import unittest
from get_dictionary_data import *

class MyTestCase(unittest.TestCase):
    def test_get_result_int(self):
        result = get_result(123)
        self.assertEqual(result, None)

    def test_get_result_bool(self):
        result = get_result(True)
        self.assertEqual(result.status_code, 200)

    def test_get_result_float(self):
        result = get_result(2.3567)
        self.assertEqual(result, None)

    def test_get_result_None(self):
        result = get_result(None)
        self.assertEqual(result.status_code, 200)

    def test_get_result_char(self):
        result = get_result('C')
        self.assertEqual(result.status_code, 200)

    def test_get_result_fuzz(self):
        result = get_result('CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC')
        self.assertEqual(result,None)

    def test_get_meaning_int(self):
        result = get_meaning(get_result(123))
        self.assertEqual(isinstance(result, str),True)

    # As we have checked all the status codes, we need not check inside individual functions

if __name__ == '__main__':
    unittest.main()
