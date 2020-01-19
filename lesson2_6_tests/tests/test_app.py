import unittest
import json
import app
from unittest.mock import patch


documents = []
directories = {}


def setUpModule():
    with open('../fixtures/documents.json', 'r', encoding='utf-8') as out_docs:
        documents.extend(json.load(out_docs))
    with open('../fixtures/directories.json', 'r', encoding='utf-8') as out_dirs:
        directories.update(json.load(out_dirs))


@patch('app.documents', documents, create=True)
@patch('app.directories', directories, create=True)
class TestAppProgram(unittest.TestCase):

    def setUp(self):
        self.example_set = {
            'shelf': '33',
            'doc': '11-2'
        }
        self.example_set2 = {
            'shelf': '1',
            'doc': '11-2'
        }

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(app.get_all_doc_owners_names(), set)
        self.assertGreater(len(app.get_all_doc_owners_names()), 0)

    def test_append_doc_to_shelf(self):
        app.append_doc_to_shelf(self.example_set['doc'], self.example_set['shelf'])
        self.assertIn(self.example_set['doc'], directories.get(self.example_set['shelf']))

    def test_delete_doc(self):
        self.assertTrue(app.check_document_existance("11-2"))

        with patch('app.input', return_value="11-2"):
            app.delete_doc()

        self.assertFalse(app.check_document_existance("11-2"))

    def test_get_doc_owner_name(self):
        with patch('app.input', return_value="11-2"):
            app.get_doc_owner_name()

    def test_check_document_existance(self):
        self.assertTrue(app.check_document_existance("10006"))

    def test_remove_doc_from_shelf(self):
        app.remove_doc_from_shelf("11-2")
        self.assertNotIn(self.example_set2['doc'], directories.get(self.example_set2['shelf']))

    def test_add_new_shelf(self):
        with patch('app.input', return_value="4"):
            app.add_new_shelf()
        self.assertIn('4', directories.keys())

    def test_get_doc_shelf(self):
        self.assertTrue(app.check_document_existance("10006"))
        with patch('app.input', return_value="10006"):
            self.assertEqual(app.get_doc_shelf(), '2')


if __name__ == '__main__':
    unittest.main()
