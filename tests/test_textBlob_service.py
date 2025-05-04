# tests/test_textBlob_service.py
import unittest
from app.services.textBlob_service import TextBlobService

class TestTextBlobService(unittest.TestCase):

    def setUp(self):
        self.service = TextBlobService()

    def test_positive_sentiment(self):
        message = "I am very happy"
        result = self.service.get_sentiment(message)
        self.assertEqual(result['sentiment'], 'positivo')
        self.assertGreater(result['polarity'], 0)

    def test_negative_sentiment(self):
        message = "I am very sad"
        result = self.service.get_sentiment(message)
        self.assertEqual(result['sentiment'], 'negativo')
        self.assertLess(result['polarity'], 0)

    def test_neutral_sentiment(self):
        message = "Today is a day"
        result = self.service.get_sentiment(message)
        self.assertEqual(result['sentiment'], 'neutro')
        self.assertAlmostEqual(result['polarity'], 0, delta=0.1)

    def test_no_text_provided(self):
        with self.assertRaises(TypeError):
            self.service.get_sentiment(None)

if __name__ == '__main__':
    unittest.main()