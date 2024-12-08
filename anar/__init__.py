from .preprocessor import TextPreprocessor
from .narrative_analyzer import NarrativeAnalyzer
from .cultural_processor import CulturalProcessor
from .graph_builder import GraphBuilder

class ANARSystem:
    """Main ANAR system class combining all components."""
    
    def __init__(self, config: Dict = None):
        self.config = config or {}
        self.preprocessor = TextPreprocessor(config)
        self.narrative_analyzer = NarrativeAnalyzer(config)
        self.cultural_processor = CulturalProcessor(config)
        self.graph_builder = GraphBuilder(config)
        
    def process_text(self, text: str) -> Dict:
        """Process Arabic text through the complete ANAR pipeline.
        
        Args:
            text: Raw Arabic text input
            
        Returns:
            Dictionary containing complete analysis results
        """
        # Preprocess text
        processed = self.preprocessor.process(text)
        
        # Analyze narrative structure
        narrative_analysis = self.narrative_analyzer.analyze(processed)
        
        # Process cultural elements
        cultural_analysis = self.cultural_processor.process(processed)
        
        # Build comprehensive graph
        narrative_graph = self.graph_builder.build_narrative_graph(
            narrative_analysis,
            cultural_analysis
        )
        
        # Build character network
        character_graph = self.graph_builder.build_character_graph(
            narrative_analysis
        )
        
        return {
            'processed_text': processed,
            'narrative_analysis': narrative_analysis,
            'cultural_analysis': cultural_analysis,
            'narrative_graph': narrative_graph,
            'character_graph': character_graph
        }
