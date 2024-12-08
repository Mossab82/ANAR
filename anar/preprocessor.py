import re
from typing import Dict, List, Tuple
from camel_tools.utils.normalize import normalize_unicode
from camel_tools.tokenizers.word import simple_word_tokenize

class TextPreprocessor:
    """Preprocessor for Classical Arabic texts."""
    
    def __init__(self, config: Dict = None):
        self.config = config or {}
        
    def process(self, text: str) -> Dict:
        """Process raw text through the preprocessing pipeline.
        
        Args:
            text: Raw Arabic text input
            
        Returns:
            Dict containing processed text and metadata
        """
        # Unicode normalization
        normalized = normalize_unicode(text)
        
        # Tokenization
        tokens = simple_word_tokenize(normalized)
        
        # Detect frame markers
        frame_markers = self._detect_frame_markers(normalized)
        
        # Detect cultural markers
        cultural_markers = self._detect_cultural_markers(normalized)
        
        return {
            'normalized_text': normalized,
            'tokens': tokens,
            'frame_markers': frame_markers,
            'cultural_markers': cultural_markers
        }
        
    def _detect_frame_markers(self, text: str) -> List[Tuple[str, int]]:
        """Detect frame story markers in the text.
        
        Args:
            text: Normalized Arabic text
            
        Returns:
            List of (marker, position) tuples
        """
        markers = []
        
        # Common frame markers
        frame_patterns = [
            r'قالت شهرزاد',
            r'وأدرك شهرزاد الصباح',
            r'حكى أن',
            r'وحدثني أيها الملك'
        ]
        
        for pattern in frame_patterns:
            for match in re.finditer(pattern, text):
                markers.append((match.group(), match.start()))
                
        return sorted(markers, key=lambda x: x[1])
        
    def _detect_cultural_markers(self, text: str) -> List[Dict]:
        """Detect cultural markers and references.
        
        Args:
            text: Normalized Arabic text
            
        Returns:
            List of cultural marker dictionaries
        """
        markers = []
        
        # Common cultural patterns
        cultural_patterns = {
            'historical_era': [
                r'في عهد [^،.]+',
                r'زمن [^،.]+'
            ],
            'social_custom': [
                r'قبّل الأرض',
                r'ضرب في الأرض'
            ],
            'idiomatic': [
                r'بين حانا ومانا',
                r'يضرب أخماساً في أسداس'
            ]
        }
        
        for marker_type, patterns in cultural_patterns.items():
            for pattern in patterns:
                for match in re.finditer(pattern, text):
                    markers.append({
                        'type': marker_type,
                        'text': match.group(),
                        'position': match.start()
                    })
                    
        return sorted(markers, key=lambda x: x['position'])
