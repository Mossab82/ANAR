import unittest
from anar.cultural_processor import CulturalProcessor

class TestCulturalProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = CulturalProcessor()
        
    def test_pattern_detection(self):
        processed_text = {
            'normalized_text': "ضرب في الأرض يطلب الربح والتجارة"
        }
        
        result = self.processor.process(processed_text)
        
        self.assertTrue(len(result['patterns']) > 0)
        self.assertTrue(any(p['category'] == 'idiomatic' for p in result['patterns']))
        
    def test_pattern_validation(self):
        processed_text = {
            'normalized_text': "وكان في عهد هارون الرشيد تاجر عظيم"
        }
        
        result = self.processor.process(processed_text)
        patterns = result['patterns']
        
        self.assertTrue(all(p['confidence'] >= 0.85 for p in patterns))
        
    def test_context_mapping(self):
        processed_text = {
            'normalized_text': """في عهد هارون الرشيد كان تاجر
            قبّل الأرض بين يدي الملك"""
        }
        
        result = self.processor.process(processed_text)
        contexts = result['contexts']
        
        self.assertTrue(len(contexts['temporal']) > 0)
        self.assertTrue(len(contexts['social']) > 0)

