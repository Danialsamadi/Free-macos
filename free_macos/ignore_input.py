import sys
import termios
import tty
import os

def ignore_keyboard_input():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setcbreak(fd)
    try:
        while True:
            os.read(fd, 1)
    except Exception:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
