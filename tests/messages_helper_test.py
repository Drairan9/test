import unittest

from helpers.messages_helper import DiscordHelperMessages


class MessagesHelperTest(unittest.TestCase):
    def test_rsi_alert_message(self):
        message = DiscordHelperMessages().get_rsi_alert_message(23.12, 30, 70)
        self.assertEqual(message, "Low rsi alert, rsi: 23.12")

        message2 = DiscordHelperMessages().get_rsi_alert_message(84.79, 30, 70)
        self.assertEqual(message2, "High rsi alert, rsi: 84.79")


if __name__ == '__main__':
    unittest.main()
