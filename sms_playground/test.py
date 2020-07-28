import unittest
from whatsapp_sender import whatsapp_send


class MyTestCase(unittest.TestCase):
    def test_message_data_int(self):
        result = whatsapp_send(123)
        self.assertEqual(result,None)

    def test_message_data_bool(self):
        result = whatsapp_send(True)
        self.assertEqual(result, None)

    def test_message_data_list(self):
        result = whatsapp_send(['wasim','salim'])
        self.assertEqual(result, '[!]Can Not send the message in list or set format.')

#Make an exception for dictionary


if __name__ == '__main__':
    unittest.main()
