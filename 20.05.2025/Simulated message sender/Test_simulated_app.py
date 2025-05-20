import unittest
from unittest.mock import patch
from SimulatedApp import is_valid_email, send_message

class TestEmailSender(unittest.TestCase):

    def test_valid_emails(self):
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("user.name@mail.co.uk"))

    def test_invalid_emails(self):
        self.assertFalse(is_valid_email("userexample.com"))
        self.assertFalse(is_valid_email("user@"))
        self.assertFalse(is_valid_email("@example.com"))
        self.assertFalse(is_valid_email("user@example"))

    @patch("builtins.print")
    def test_send_message_success(self, mock_print):
        result = send_message("test@mail.com", "Hello there")
        self.assertEqual(result, "Съобщението беше успешно изпратено.")
        mock_print.assert_any_call("Изпращане на съобщение до: test@mail.com")
        mock_print.assert_any_call("Съобщение: Hello there")

    @patch("builtins.print")
    def test_send_message_fail(self, mock_print):
        result = send_message("bademail.com", "Oops")
        self.assertEqual(result, "Невалиден имейл адрес.")
        mock_print.assert_not_called()

if __name__ == '__main__':
    unittest.main()
