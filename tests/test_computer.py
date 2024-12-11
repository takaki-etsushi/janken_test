import unittest
from unittest.mock import patch
from source.computer import computer_pon

class TestComputerPon(unittest.TestCase):
    @patch("random.choice", return_value="グー")
    def test_random_choice_1(self, mock_choice):
        result = computer_pon()
        self.assertEqual(result, "グー")

    @patch("random.choice", return_value="チョキ")
    def test_random_choice_2(self, mock_choice):
        result = computer_pon()
        self.assertEqual(result, "チョキ")

    @patch("random.choice", return_value="パー")
    def test_random_choice_3(self, mock_choice):
        result = computer_pon()
        self.assertEqual(result, "パー")