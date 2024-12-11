import unittest
from unittest.mock import patch
from source.player import player_pon

class TestPlayerPon(unittest.TestCase):
    @patch("builtins.input", return_value="1")
    def test_input_1(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "グー")

    @patch("builtins.input", return_value="2")
    def test_input_2(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "チョキ")

    @patch("builtins.input", return_value="3")
    def test_input_3(self, mock_input):
        result = player_pon()
        self.assertEqual(result, "パー")

    @patch("builtins.input", side_effect = ["0", "4", "1"])
    def test_input_0_4(self, mock_input):
        with patch("builtins.print") as mock_print:
            result = player_pon()
            self.assertEqual(result, "グー")
            mock_print.assert_any_call("不正な入力です。もう一度入力してください。")
            mock_print.assert_any_call("不正な入力です。もう一度入力してください。")

