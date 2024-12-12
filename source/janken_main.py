from . import player
from . import computer
from . import janken_judge

def play_round(round_number):
    print(f"-----ラウンド {round_number} -----")
    computer_hand = computer.computer_pon()
    player_hand = player.player_pon()
    result = janken_judge.judge(computer_hand, player_hand)

    print(f"あなたの手:{player_hand}")
    print(f"コンピューターの手:{computer_hand}")
    print("")

    if result == 'draw':
        print("あいこです！ 再度対決！")
        return None
    elif result == 'player_win':
        print("あなたの勝ちです！")
        return 'player_win'
    else:
        print("コンピューターの勝ちです！")
        return 'computer_win'

def print_final_result(player_win, computer_win):
    print("【最終結果】")
    print(f"あなた:{player_win}勝")
    print(f"コンピュータ:{computer_win}勝")
    if player_win > computer_win:
        print("あなたの総合勝利です！")
    else:
        print("コンピュータの総合勝利です！")

def main():
    player_win = 0
    computer_win = 0
    round_number = 1

    while round_number <= 3:
        result = play_round(round_number)
        if result is not None:
            round_number += 1
            if result == 'player_win':
                player_win += 1
            elif result == 'computer_win':
                computer_win += 1

    print_final_result(player_win, computer_win)

if __name__ == '__main__':
    main()