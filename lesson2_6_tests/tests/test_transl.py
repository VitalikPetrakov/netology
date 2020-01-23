import unittest
import requests
import transl
from unittest.mock import patch


class TestTranslProgram(unittest.TestCase):
    def setUp(self):
        self.params = {
        'key': transl.API_KEY,
        'text': 'hello',
        'lang': 'ru',
    }

