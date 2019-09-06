import unittest
import json
import lesson2_6_tests.secretar as programm
from unittest.mock import patch

documents = []
directories = {}


def setUpModule():
    with open('../fixtures/documents.json', 'r', encoding='utf-8') as out_docs:
        documents.extend(json.load(out_docs))
        print(documents)
    with open('../fixtures/directories.json', 'r', encoding='utf-8') as out_dirs:
        directories.update(json.load(out_dirs))
        print(directories)


@patch('lesson2_6_tests.fixtures.documents', documents, create=True)
@patch('lesson2_6_tests.fixtures.directories', directories, create=True)
class TestSecretaryProgram(unittest.TestCase):

    def setUp(self):
        self.example_set = {
            'shelf': 33,
            'doc': 22
        }

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(programm.get_all_doc_owners_names(), set)
        self.assertGreater(len(programm.get_all_doc_owners_names()), 0)

    def test_append_doc_to_shelf(self):
        programm.append_doc_to_shelf(self.example_set['doc'], self.example_set['shelf'])
        self.assertIn(self.example_set['doc'], directories.get(self.example_set['shelf']))

    def test_delete_doc(self):
        self.assertTrue(programm.check_document_existance("11-2"))

        with patch('programm.input', return_value="11-2"):
            programm.delete_doc()

        self.assertFalse(programm.check_document_existance("11-2"))


if __name__ == '__main__':
    unittest.main()