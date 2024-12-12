import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'source')))
import unittest
from unittest.mock import patch
import source.janken_main 


class TestJanken(unittest.TestCase):
    @patch('source.computer.computer_pon', return_value='グー')
    @patch('source.player.player_pon', return_value='チョキ')
    def test_play_round_player_win(self, mock_player, mock_computer):
        result = source.janken_main.play_round(1)
        self.assertEqual(result, 'computer_win')

    @patch('source.computer.computer_pon', return_value='グー')
    @patch('source.player.player_pon', return_value='パー')
    def test_play_round_computer_win(self, mock_player, mock_computer):
        result = source.janken_main.play_round(1)
        self.assertEqual(result, 'player_win')

    @patch('source.computer.computer_pon', return_value='グー')
    @patch('source.player.player_pon', return_value='グー')
    def test_play_round_draw(self, mock_player, mock_computer):
        result = source.janken_main.play_round(1)
        self.assertIsNone(result)