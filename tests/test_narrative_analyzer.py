import unittest
from anar.narrative_analyzer import NarrativeAnalyzer

class TestNarrativeAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = NarrativeAnalyzer()
        
    def test_narrative_element_extraction(self):
        processed_text = {
            'normalized_text': "قال الملك شهريار للوزير: اجلب لي شهرزاد",
            'frame_markers': [("قال الملك", 0)]
        }
        
        result = self.analyzer.analyze(processed_text)
        
        self.assertTrue(len(result['nested_stories']) > 0)
        self.assertIsNotNone(result['narrative_graph'])
        
    def test_character_network_analysis(self):
        processed_text = {
            'normalized_text': """قال الملك شهريار للوزير: اجلب لي شهرزاد.
            فقالت شهرزاد: كان تاجر يحكي للملك قصة""",
            'frame_markers': [("قال الملك", 0), ("فقالت شهرزاد", 50)]
        }
        
        result = self.analyzer.analyze(processed_text)
        char_network = result['character_network']
        
        self.assertTrue(char_network.number_of_nodes() > 0)
        self.assertTrue(char_network.number_of_edges() > 0)
