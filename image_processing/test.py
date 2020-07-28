import unittest
import main

class MyTestCase(unittest.TestCase):
    def test_number(self):
        result = main.convert_image([1,2])
        self.assertEqual(result,None)
    def test_none(self):
        result = main.convert_image(['PokeDex',None])
        self.assertEqual(result,None)

    def test_bool(self):
        result = main.convert_image(['PokeDex',True])
        self.assertEqual(result,None)
if __name__ == '__main__':
    unittest.main()
