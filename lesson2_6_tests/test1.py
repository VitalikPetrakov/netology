import unittest
import json
import secretar
from unittest.mock import patch


documents = []
directories = {}


def setUpModule():
    with open('fixtures/documents.json', 'r', encoding='utf-8') as out_docs:
        documents.extend(json.load(out_docs))
    with open('fixtures/directories.json', 'r', encoding='utf-8') as out_dirs:
        directories.update(json.load(out_dirs))


@patch('prog.documents', documents, create=True)
@patch('prog.directories', directories, create=True)
class TestSecretaryProgram(unittest.TestCase):

    def setUp(self):
        self.example_set = {
            'shelf': 33,
            'doc': 22
        }

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(secretar.get_all_doc_owners_names(), set)
        self.assertGreater(len(secretar.get_all_doc_owners_names()), 0)

    def test_append_doc_to_shelf(self):
        secretar.append_doc_to_shelf(self.example_set['doc'], self.example_set['shelf'])
        self.assertIn(self.example_set['doc'], directories.get(self.example_set['shelf']))

    def test_delete_doc(self):
        self.assertTrue(secretar.check_document_existance("11-2"))

        with patch('programm.input', return_value="11-2"):
            secretar.delete_doc()

        self.assertFalse(secretar.check_document_existance("11-2"))


if __name__ == '__main__':
    unittest.main()
