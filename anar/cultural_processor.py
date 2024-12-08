from typing import Dict, List
import re

class CulturalProcessor:
    """Processor for cultural elements in Classical Arabic texts."""
    
    def __init__(self, config: Dict = None):
        self.config = config or {}
        self.cultural_patterns = self._load_cultural_patterns()
        
    def process(self, processed_text: Dict) -> Dict:
        """Process text for cultural elements and patterns.
        
        Args:
            processed_text: Output from TextPreprocessor
            
        Returns:
            Dict containing cultural analysis results
        """
        text = processed_text['normalized_text']
        
        # Detect patterns
        patterns = self._detect_patterns(text)
        
        # Validate patterns
        validated_patterns = self._validate_patterns(patterns)
        
        # Map contexts
        contexts = self._map_contexts(validated_patterns, text)
        
        return {
            'patterns': validated_patterns,
            'contexts': contexts
        }
        
    def _load_cultural_patterns(self) -> Dict:
        """Load cultural pattern definitions.
        
        Returns:
            Dictionary of pattern categories and their patterns
        """
        return {
            'idiomatic': {
                'ضرب في الأرض': {
                    'meaning': 'to travel extensively',
                    'context': 'travel_narrative'
                },
                'بين حانا ومانا': {
                    'meaning': 'between a rock and a hard place',
                    'context': 'difficulty'
                }
            },
            'historical': {
                'في عهد هارون الرشيد': {
                    'period': 'Abbasid',
                    'year_range': (786, 809)
                }
            },
            'social_custom': {
                'قبّل الأرض بين يديه': {
                    'meaning': 'show deep respect',
                    'context': 'court_etiquette'
                }
            }
        }
        
    def _detect_patterns(self, text: str) -> List[Dict]:
        """Detect cultural patterns in text.
        
        Args:
            text: Normalized Arabic text
            
        Returns:
            List of detected pattern dictionaries
        """
        detected = []
        
        for category, patterns in self.cultural_patterns.items():
            for pattern, info in patterns.items():
                for match in re.finditer(re.escape(pattern), text):
                    detected.append({
                        'category': category,
                        'pattern': pattern,
                       'position': match.start(),
                        'info': info,
                        'context_window': text[max(0, match.start()-50):
                                             min(len(text), match.end()+50)]
                    })
                    
        return detected
        
    def _validate_patterns(self, patterns: List[Dict]) -> List[Dict]:
        """Validate detected cultural patterns.
        
        Args:
            patterns: List of detected patterns
            
        Returns:
            List of validated pattern dictionaries
        """
        validated = []
        
        for pattern in patterns:
            confidence = self._calculate_confidence(pattern)
            
            if confidence >= 0.85:  # Threshold from paper
                pattern['confidence'] = confidence
                validated.append(pattern)
                
        return validated
        
    def _calculate_confidence(self, pattern: Dict) -> float:
        """Calculate confidence score for a pattern.
        
        Args:
            pattern: Pattern dictionary
            
        Returns:
            Confidence score between 0 and 1
        """
        # Base confidence
        confidence = 0.5
        
        # Adjust based on context
        if pattern['category'] == 'idiomatic':
            # Check if context matches expected usage
            expected_context = pattern['info']['context']
            if expected_context in pattern['context_window'].lower():
                confidence += 0.3
                
        elif pattern['category'] == 'historical':
            # Check for additional temporal markers
            if re.search(r'في (عهد|زمن|وقت)', pattern['context_window']):
                confidence += 0.3
                
        elif pattern['category'] == 'social_custom':
            # Check for social interaction markers
            if re.search(r'(الملك|السلطان|الوزير)', pattern['context_window']):
                confidence += 0.3
                
        # Add context coherence bonus
        if len(pattern['context_window'].split()) >= 5:
            confidence += 0.2
            
        return min(1.0, confidence)
        
    def _map_contexts(self, patterns: List[Dict], text: str) -> Dict:
        """Map cultural patterns to their broader contexts.
        
        Args:
            patterns: List of validated patterns
            text: Full normalized text
            
        Returns:
            Dictionary of contextual mappings
        """
        contexts = {
            'temporal': [],
            'social': [],
            'cultural': []
        }
        
        for pattern in patterns:
            if pattern['category'] == 'historical':
                contexts['temporal'].append({
                    'period': pattern['info']['period'],
                    'years': pattern['info']['year_range'],
                    'text': pattern['pattern']
                })
                
            elif pattern['category'] == 'social_custom':
                contexts['social'].append({
                    'custom': pattern['pattern'],
                    'meaning': pattern['info']['meaning'],
                    'context': pattern['info']['context']
                })
                
            elif pattern['category'] == 'idiomatic':
                contexts['cultural'].append({
                    'expression': pattern['pattern'],
                    'meaning': pattern['info']['meaning'],
                    'usage': pattern['info']['context']
                })
                
        return contexts

