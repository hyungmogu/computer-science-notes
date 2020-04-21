"""CSC148 Lab 3: Inheritance

=== CSC148 Fall 2019 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the implementation of a simple number game.
The key class design feature here is *inheritance*, which is used to enable
different types of players, both human and computer, for the game.
"""
from __future__ import annotations
import random
from typing import Tuple
import re

class Player:
    """A player in number game

    === Attributes ===
    name:
        The name of player

    === Representation invariants ===
    - len(name.strip()) != 0
    - 0 <= self.current <= self.goal
    - 0 < self.min_step <= self.max_step <= self.goal
    """
    name: str

    def __init__(self, name: str) -> None:
        """Initialize this Player

            Precondition:
                - len(name.strip()) != 0
        """
        self.name = name

    def move(self, current: int, min_step: int,
             max_step: int, goal: int) -> int:
        """Return amount of steps taken by a player

            Precondition:
                - 0 < min_step <= max_step <= goal
                - 0 <= self.current <= self.goal
        """
        raise NotImplementedError

class RandomPlayer(Player):

    def move(self, current: int, min_step: int,
             max_step: int, goal: int) -> int:
        return random.randint(min_step, max_step)


class UserPlayer(Player):

    def move(self, current: int, min_step: int,
             max_step: int, goal: int) -> int:

        amount = 0

        while True:
            amount_raw = input('Enter step amount ({}-{})'.format(min_step, max_step))

            if len(amount_raw.strip()) == 0:
                print('Please select integer value between {} and {}'.format(min_step, max_step))
                continue

            if re.search(r'[^0-9]+', amount_raw):
                print('Please select integer value between {} and {}'.format(min_step, max_step))
                continue

            amount = int(amount_raw)
            if amount < min_step or amount > max_step:
                print('Please select steps between {} and {}'.format(min_step, max_step))
                continue

            break

        return amount

# =============== SOLUTION (Task 8.2) ================

class StrategicPlayer(Player):

    def move(self, current: int, min_step: int,
             max_step: int, goal: int) -> int:

        return 3
# ====================================================


class NumberGame:
    """A number game for two players.

    A count starts at 0. On a player's turn, they add to the count an amount
    between a set minimum and a set maximum. The player who brings the count
    to a set goal amount is the winner.

    The game can have multiple rounds.

    === Attributes ===
    goal:
        The amount to reach in order to win the game.
    min_step:
        The minimum legal move.
    max_step:
        The maximum legal move.
    current:
        The current value of the game count.
    players:
        The two players.
    turn:
        The turn the game is on, beginning with turn 0.
        If turn is even number, it is players[0]'s turn.
        If turn is any odd number, it is player[1]'s turn.

    === Representation invariants ==
    - self.turn >= 0
    - 0 <= self.current <= self.goal
    - 0 < self.min_step <= self.max_step <= self.goal
    """
    goal: int
    min_step: int
    max_step: int
    current: int
    players: Tuple[Player, Player]
    turn: int

    def __init__(self, goal: int, min_step: int, max_step: int,
                 players: Tuple[Player, Player]) -> None:
        """Initialize this NumberGame.

        Precondition: 0 < min_step <= max_step <= goal
        """
        self.goal = goal
        self.min_step = min_step
        self.max_step = max_step
        self.current = 0
        self.players = players
        self.turn = 0

    def play(self) -> str:
        """Play one round of this NumberGame. Return the name of the winner.

        A "round" is one full run of the game, from when the count starts
        at 0 until the goal is reached.
        """
        while self.current < self.goal:
            self.play_one_turn()
        # The player whose turn would be next (if the game weren't over) is
        # the loser. The one who went one turn before that is the winner.
        winner = self.whose_turn(self.turn - 1)
        return winner.name

    def whose_turn(self, turn: int) -> Player:
        """Return the Player whose turn it is on the given turn number.
        """
        if turn % 2 == 0:
            return self.players[0]
        else:
            return self.players[1]

    def play_one_turn(self) -> None:
        """Play a single turn in this NumberGame.

        Determine whose move it is, get their move, and update the current
        total as well as the number of the turn we are on.
        Print the move and the new total.
        """
        next_player = self.whose_turn(self.turn)
        amount = next_player.move(
            self.current,
            self.min_step,
            self.max_step,
            self.goal
        )
        self.current += amount
        self.turn += 1

        print(f'{next_player.name} moves {amount}.')
        print(f'Total is now {self.current}.')


# TODO: Write classes Player, RandomPlayer, UserPlayer, and StrategicPlayer.
def make_player(generic_name: str) -> Player:
    """Return a new Player based on user input.

    Allow the user to choose a player name and player type.
    <generic_name> is a placeholder used to identify which player is being made.
    """
    name = input(f'Enter a name for {generic_name}: ')
    # TODO: Create and return some sort of Player.
    # =============== SOLUTION (Task 8.1) ================
    player_type_list = ['r', 'u', 's']

    while True:
        player_type = input(
            'Enter player type '
            '(r - Random Player, u - User Player, s - Strategic Player)')

        if player_type not in player_type_list:
            print('Please select one of the three values '
                  '({})'.format(','.join(player_type_list)))
            continue

        break

    if player_type == 'u':
        return UserPlayer(name)
    elif player_type == 's':
        return StrategicPlayer(name)
    elif player_type == 'r':
        return RandomPlayer(name)

    # ====================================================

def main() -> None:
    """Play multiple rounds of a NumberGame based on user input settings.
    """
    goal = int(input('Enter goal amount: '))
    minimum = int(input('Enter minimum move: '))
    maximum = int(input('Enter maximum move: '))
    p1 = make_player('p1')
    p2 = make_player('p2')
    while True:
        g = NumberGame(goal, minimum, maximum, (p1, p2))
        winner = g.play()
        print(f'And {winner} is the winner!!!')
        print(p1)
        print(p2)
        again = input('Again? (y/n) ')
        if again != 'y':
            return


if __name__ == '__main__':
    # Uncomment the lines below to check your work using
    # python_ta and doctest.
    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['random'],
    #     'allowed-io': [
    #         'main',
    #         'make_player',
    #         'move',
    #         'play_one_turn'
    #     ]
    # })
    main()