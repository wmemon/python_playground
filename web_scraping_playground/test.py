import unittest
import hackernews


class MyTestCase(unittest.TestCase):
    def test_greater_than_hundred_None(self):
        result = hackernews.greater_than_hundred(None)
        self.assertEqual(result, "We encountered a problem, Please check your internet connection and link.")

    def test_greater_than_hundred_int(self):
        result = hackernews.greater_than_hundred(100)
        self.assertEqual(result, "We encountered a problem, Please check your internet connection and link.")

    def test_greater_than_hundred_char(self):
        result = hackernews.greater_than_hundred('a')
        self.assertEqual(result, "We encountered a problem, Please check your internet connection and link.")

    def test_greater_than_hundred_str(self):
        result = hackernews.greater_than_hundred('wasim')
        self.assertEqual(result, "We encountered a problem, Please check your internet connection and link.")

    def test_greater_than_hundred_bad_list(self):
        result = hackernews.greater_than_hundred([1, 2, 3, 4, 5])
        self.assertEqual(result, "We encountered a problem, Please check your internet connection and link.")

    def test_greater_than_hundred_bad_list_str(self):
        result = hackernews.greater_than_hundred(['wasim', 'mehzabeen'])
        self.assertEqual(result, "We encountered a problem, Please check your internet connection and link.")


if __name__ == '__main__':
    unittest.main()
