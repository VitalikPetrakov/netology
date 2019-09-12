import unittest
from lesson2_6_tests.tests import test1


def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(
      test1.TestSecretaryProgram
    )
    suite.addTests(tests)
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())