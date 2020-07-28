import unittest
from whatsapp_sender import whatsapp_send


class MyTestCase(unittest.TestCase):
    def test_message_data_int(self):
        result = whatsapp_send(123)
        self.assertEqual(result,None)


if __name__ == '__main__':
    unittest.main()
