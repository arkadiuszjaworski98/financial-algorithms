import re


def validate_digits(input):
    if re.match('\d+$', str(input)):
        return True
    else:
        return False


def validate_menu_options(input, options):
    menu_options = ''
    for i in input:
        if validate_digits(i):
            menu_options += str(i)

    if menu_options != '':
        if re.match(f'([{menu_options}])$', str(options)):
            return True
        else:
            return False
