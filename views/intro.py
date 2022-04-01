import sys

from views.consoleClear import clear


def views_intro(name, controller):
    clear()
    print(f'Welcome to the {name}.\n')
    answer = input('Press 1 to start.\nPress any key to exit: ')
    if answer == '1':
        clear()
        controller()
    else:
        sys.exit()
