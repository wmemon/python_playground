import unittest
from mailchecker import check_mail_valid

class MyTestCase(unittest.TestCase):
    def test_mail_check_valid_disposable(self):
        result = check_mail_valid('4winte@braginun.ml')
        self.assertEqual(result,True)

    def test_mail_check_valid_real(self):
        result = check_mail_valid('memwasim00@gmail.com')
        self.assertEqual(result, False)

    def test_mail_check_valid_int(self):
        result = check_mail_valid(123)
        self.assertEqual(result, None)

    def test_mail_check_valid_bool(self):
        result = check_mail_valid(True)
        self.assertEqual(result, None)

    def test_mail_check_valid_list(self):
        result = check_mail_valid(['wasim','salim'])
        self.assertEqual(result, None)

    def test_mail_check_valid_dict(self):
        result = check_mail_valid({'name':'wasim', 'age':5})
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
