# https://mobile.twitter.com/deathbybadger/status/1567425842526945280/photo/1

from gameplay.Game import Game
from gameplay.Player import Player


def main():
    player = Player("Forrest")
    game = Game(player, typing_speed=100)

    game.run()


if __name__ == "__main__":
    main()