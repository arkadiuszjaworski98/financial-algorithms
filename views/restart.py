import sys

from views.consoleClear import clear


def restart(message, algorithm):
    clear()
    print(message)
    answer = input('Press 1 to restart.\nPress any key to exit: ')
    if answer == '1':
        clear()
        algorithm()
    else:
        sys.exit()
