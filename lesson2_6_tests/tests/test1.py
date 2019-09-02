import unittest
from lesson2_6_tests.secretar import check_document_existance
import os
import json
import tempfile

class MyTestCase(unittest.TestCase):
    """Тест для функции check_document_existance"""

    def setUp(self):
        self.tempfile = tempfile.TemporaryFile()
        # current_path = str(os.path.dirname(os.path.abspath(__file__)))
        # f_documents = os.path.join(current_path, '../fixtures/documents.json')
        # with open(f_documents, 'r') as self.out_docs:
        #     self.documents = json.load(self.out_docs)

    def tearDown(self):
        self.tempfile.close()

    def test_check_document_existance(self):

        self.resalt_cheking = check_document_existance("10006")
        self.assertEqual(self.resalt_cheking, True)


if __name__ == '__main__':
    unittest.main()

# import unittest
# import json
# import app
# from mock import patch
#
# documents = []
# directories = {}
#
#
# def setUpModule():
#     with open('fixtures/documents.json', 'r', encoding='utf-8') as out_docs:
#         documents.extend(json.load(out_docs))
#     with open('fixtures/directories.json', 'r', encoding='utf-8') as out_dirs:
#         directories.update(json.load(out_dirs))
#
#
# @patch('app.documents', documents, create=True)
# @patch('app.directories', directories, create=True)
# class TestSecretaryProgram(unittest.TestCase):
#
#     def setUp(self):
#         self.example_set = {
#             'shelf': 33,
#             'doc': 22
#         }
#
#     def test_get_all_doc_owners_names(self):
#         self.assertIsInstance(app.get_all_doc_owners_names(), set)
#         self.assertGreater(len(app.get_all_doc_owners_names()), 0)
#
#     def test_append_doc_to_shelf(self):
#         app.append_doc_to_shelf(self.example_set['doc'], self.example_set['shelf'])
#         self.assertIn(self.example_set['doc'], directories.get(self.example_set['shelf']))
#
#     def test_delete_doc(self):
#         self.assertTrue(app.check_document_existance("11-2"))  # check before deleting doc
#
#         with patch('app.input', return_value="11-2") as child1:
#             app.delete_doc()
#
#         self.assertFalse(app.check_document_existance("11-2"))  # check after deleting doc
#
#
# if __name__ == '__main__':
#     unittest.main()