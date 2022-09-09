import sys
import time
import random


def slow_print(text: str, typing_speed: int = 50):
    """
    Simulates human typing to stdout
    """
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()

        sleep_time = (random.random() * 10.0) / typing_speed
        time.sleep(sleep_time)

    print('')
