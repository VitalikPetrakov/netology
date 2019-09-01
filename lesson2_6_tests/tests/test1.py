import unittest
from lesson2_6_tests.secretar import check_document_existance
import os



class MyTestCase(unittest.TestCase):
    """Тест для функции check_document_existance"""

    def test_check_document_existance(self):
        resalt_cheking = check_document_existance("10006")
        self.assertEqual(resalt_cheking, True)


if __name__ == '__main__':
    current_path = str(os.path.dirname(os.path.abspath(__file__)))
    f_directories = os.path.join(current_path, 'fixtures/directories.json')
    f_documents = os.path.join(current_path, 'fixtures/documents.json')
    unittest.main()

