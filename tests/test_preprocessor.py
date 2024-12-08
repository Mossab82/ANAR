import unittest
from anar.preprocessor import TextPreprocessor

class TestPreprocessor(unittest.TestCase):
    def setUp(self):
        self.preprocessor = TextPreprocessor()
        
    def test_frame_marker_detection(self):
        text = "قالت شهرزاد: وحدثني أيها الملك السعيد"
        result = self.preprocessor.process(text)
        
        self.assertTrue(len(result['frame_markers']) > 0)
        self.assertEqual(result['frame_markers'][0][0], "قالت شهرزاد")
        
    def test_cultural_marker_detection(self):
        text = "وكان في عهد هارون الرشيد تاجر ضرب في الأرض"
        result = self.preprocessor.process(text)
        
        cultural_markers = result['cultural_markers']
        self.assertTrue(any(m['type'] == 'historical_era' for m in cultural_markers))
        self.assertTrue(any(m['type'] == 'social_custom' for m in cultural_markers))
        
    def test_text_normalization(self):
        text = "قالَ الملِكُ"
        result = self.preprocessor.process(text)
        
        self.assertNotEqual(text, result['normalized_text'])
        self.assertTrue(len(result['tokens']) > 0)
