import unittest
from unittest.mock import patch
from source.janken_judge import judge

class TestJudge(unittest.TestCase):
    def test_judge(self):
        patterns = [
            ("グー", "グー", "draw"),
            ("グー", "チョキ", "computer_win"),
            ("グー", "パー", "player_win"),
            ("チョキ", "グー", "player_win"),
            ("チョキ", "チョキ", "draw"),
            ("チョキ", "パー", "computer_win"),
            ("パー", "グー", "computer_win"),
            ("パー", "チョキ", "player_win"),
            ("パー", "パー", "draw"),
        ]
        for computer_hand, player_hand, expected in patterns:
            with self.subTest(computer_hand=computer_hand, player_hand=player_hand):
                result = judge(computer_hand, player_hand)
                self.assertEqual(result, expected)
            