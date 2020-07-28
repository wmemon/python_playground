import unittest
import pdf_merger

class MyTestCase(unittest.TestCase):
    def test_merge_none(self):
        result = pdf_merger.merge_pdf([None])
        self.assertEqual(result, "[!]Enter a string as the Filename.")
    def test_merge_bool(self):
        result = pdf_merger.merge_pdf([True])
        self.assertEqual(result, "[!]Enter a string as the Filename.")

    def test_merge_incorrect_file(self):
        result = pdf_merger.merge_pdf(['1'])
        self.assertEqual(result,"[!]File not found. Recheck The FileName.")

    def test_merge_empty_list(self):
        result = pdf_merger.merge_pdf([])
        self.assertEqual(result, "[!]Please enter a list.")

    def test_merge_no_arguements(self):
        result = pdf_merger.merge_pdf()
        self.assertEqual(result, "[!]Please enter a list.")

if __name__ == '__main__':
    unittest.main()
