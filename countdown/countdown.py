from utils.printer import best_print

from time import sleep as wait
from datetime import timedelta
import sys
from random import random


def countdown_way1(nb_sec, tag):
    for i in range(nb_sec, -1, -1):
        print(f"{tag}:", timedelta(seconds=i), end="\r")
        wait(1)
    #lenght of the string "Timer Ended !" is the length of the last print. Otherwise, pb
    print("Timer Ended !      ")


def countdown_way2(nb_sec, tag):
    for i in range(nb_sec, -1, -1):
        t = f"{tag}: {timedelta(seconds=i)}"
        print(t, end="\r")
        wait(1)
    #remove the last print manually
    print(' ' * len(str(t)), end="\r")
    print("done !")


def countdown_way3(nb_sec, tag):
    printer = best_print()
    for i in range(nb_sec, -1, -1):
        printer.print(tag, timedelta(seconds=i))
        wait(1)
    #remove the last print
    printer.erase_cur_line()
    print("done !")


def test_progress():
    n = 20
    printer = best_print()
    for i in range(n):
        printer.print_progress(i + 1, n, newline=False)
        sys.stdout.flush()
        wait(0.02 * random())
    printer.print("the end !")


if __name__ == "__main__":
    countdown_way1(5, "timer1")
    countdown_way2(5, "timer2")
    countdown_way2(5, "timer3")
    print('eeeeeee', end="\r")
    wait(1)
    print("ffffffff")  #better length to erase
    print('eeeeeee', end="\r")
    wait(1)
    print("ffff")  #not enought lenth to erase
    test_progress()
