import unittest
import transl


class TestTranslProgram(unittest.TestCase):

    def test_get_response(self):
        self.assertEqual(str(transl.get_response('hello', 'en')), '<Response [200]>')

    def test_get_text_from_response(self):
        response = transl.get_response('hello', 'en')
        self.assertEqual(transl.get_text_from_response(response), 'привет')