import random


class Game:
    _RULES = {
        'rock': ('paper', 'spock'),  # камень
        'paper': ('scissors', 'lizard'),  # бумага
        'scissors': ('rock', 'spock'),  # ножницы
        'lizard': ('rock', 'scissors'),  # ящерица
        'spock': ('paper', 'lizard')  # спок
    }

    def __init__(self):
        self._round = 0
        self._player_score = 0
        self._computer_score = 0

    @staticmethod
    def _repeat():
        return input('Repeat (Y/N)?: ').lower() == 'y'

    def _is_bot_win(self, your_choice: str, bot_choice: str):
        return bot_choice in self._RULES[your_choice]

    def run(self):
        while True:
            self._round += 1
            print(f'Round {self._round}!')
            print(f'Player / Computer - '
                  f'{self._player_score} / {self._computer_score}')
            player = input('Your choice (rock paper scissors lizard spock)?: ')
            if player not in self._RULES.keys():
                print(f'Invalid input "{player}"')
                if self._repeat():
                    continue
                break
            computer = random.choice(tuple(self._RULES.keys()))
            is_bot_win = self._is_bot_win(player, computer)
            print(f'Player: {player}')
            print(f'Computer: {computer}')
            print('Computer WIN!' if is_bot_win else 'Player WIN!')
            self._player_score += int(not is_bot_win)
            self._computer_score += int(is_bot_win)
            if not self._repeat():
                break


if __name__ == '__main__':
    Game().run()
