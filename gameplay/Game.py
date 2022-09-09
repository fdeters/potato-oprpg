from .helpers.dice import Die
from .helpers.printing import slow_print
from .Player import Player
from .events import events

import time


class Game:
    def __init__(self, player: Player, typing_speed: int = 50) -> None:
        self._player = player
        self._typing_speed = typing_speed
        self.die = Die()

        self.danger_level = 1
        self._game_over = False


    def run(self):
        """
        Main game loop
        """
        while not self._game_over:
            command = self.get_command()
            match command.lower():
                case 'h':
                    self._player.hurl(self.danger_level)
                    self.slow_print("You hurl potatoes into your garden. Scram, orcs!")
                case 'e':
                    self.new_event()
                case _:
                    print(f"[{command.upper()}] is not a valid command.")
                    continue

            self.show_player_stats()
            self.check_for_game_over()
        
        # game over!
        print("GAME OVER")
        print(f"Game over types: {self.get_game_over_type()}")


    def get_command(self):
        """Get the command via user input."""
        command = input("Enter your command | [E] to roll a new event | [H] to hurl potatoes at orcs: ")
        try:
            command = command[0]
        except IndexError:
            pass
        return command


    def new_event(self):
        """Roll/execute a new event"""
        # roll on the Grass and Mud table
        roll_1 = self.die.roll()
        event_1 = events["Grass and Mud"][roll_1]
        self.slow_print(f"Event: {event_1}")

        # roll on the next table or increase danger
        if event_1 == "The World Gets Darker":
            self.slow_print("The world becomes a darker, more dangerous place. " 
                "From now on, removing an orc costs an additional potato.")
            self.increase_danger()
        else:
            roll_2 = self.die.roll()
            event_2 = events[event_1][roll_2]
            self.slow_print(event_2['description'])

            # adjust Player's scores
            self.handle_event_outcomes(event_2['outcomes'])


    def increase_danger(self) -> None:
        self.danger_level += 1
        self.slow_print(f"The danger level is now {self.danger_level}")


    def handle_event_outcomes(self, event_outcomes: list) -> None:
        for outcome in event_outcomes:
            magnitude = outcome['magnitude']
            stat = outcome['stat']
            try: 
                match stat:
                    case "destiny":
                        self._player.destiny += magnitude
                    case "potatoes":
                        self._player.potatoes += magnitude
                    case "orcs":
                        self._player.orcs += magnitude
            except ValueError:
                message = f"{stat.capitalize()} cannot be changed"
            else:
                up_or_down = "up" if magnitude > 0 else "down"
                message  = f"{stat.capitalize()} score went {up_or_down} by {abs(magnitude)}"
            finally:
                self.slow_print(message)


    def check_for_game_over(self) -> None:
        condition = self._player.destiny >= 10 or self._player.potatoes >= 10 or self._player.orcs >= 10
        self._game_over = condition


    def get_game_over_type(self) -> set:
        """
        Return the type of game over. Note that it's possibly to have hybrid ending
        scenarios, e.g. 10+ destiny AND 10+ orcs.
        """
        result = set()
        if self._player.destiny >= 10:
            result.add('destiny')
        if self._player.potatoes >= 10:
            result.add('potatoes')
        if self._player.orcs >= 10:
            result.add('orcs')

        return result

    def show_player_stats(self):
        print(str(self._player) + '\n')


    def slow_print(self, text: str):
        slow_print(text, typing_speed=self._typing_speed)
    
    @property
    def game_over(self):
        return self._game_over
    
    @property
    def game_over_type(self):
        return self._game_over_type
