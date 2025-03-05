import pyautogui

from argparse import ArgumentParser, Namespace
from PIL import Image
from time import sleep

from utils import count_execution_time, locate_and_click, locate_with_tries


@count_execution_time
def skip_turns(turns: int):
    next_turn = Image.open("images/next_turn.png")
    try:
        for _ in range(turns):
            locate_and_click(next_turn, tries=-1, clicks=2)
    finally:
        next_turn.close()


def set_battle_speed():
    battle_speed = Image.open("images/battle_speed/battle_speed.png")
    fastest = Image.open("images/battle_speed/fastest.png")
    pause = Image.open("images/pause.png")
    close = Image.open("images/close.png")

    try:
        locate_and_click(pause)

        for tries in range(4):
            try:
                locate_and_click(fastest, clicks=0)
            except pyautogui.ImageNotFoundException as e:
                if tries == 3:
                    raise e

                locate_and_click(battle_speed, tries=1, x_offset=100, confidence=1)
                sleep(0.5)
    finally:
        locate_and_click(close)
        for image in (battle_speed, fastest, pause, close):
            image.close()


def main(args: Namespace):
    if args.skip_turns:
        set_battle_speed()
        print(f"Will skip {args.skip_turns} turns")
        skip_turns(args.skip_turns)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--skip_turns", default=False, type=int, help="Number of turns to skip")
    # TODO: implement Baraquel abilities cheese
    # parser.add_argument("--use_abilities", default=False, type=int, help="Number of times to use abilities")
    args = parser.parse_args()
    main(args)
