import time
import os


def cls():
    os.system('clear'
              if os.name == 'posix'
              else 'cls')


def printText():
    text = "Hello world!"
    while True:
        lines = os.get_terminal_size().lines - 2
        for i in range(0, lines):
            cls()
            print("\n" * i + text)
            time.sleep(0.25)
        for i in range(lines, 0, -1):
            cls()
            print("\n" * i + text)
            time.sleep(0.25)

printText()