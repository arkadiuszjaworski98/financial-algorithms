from views.algorithms.BSM import views_black_scholes_merton
from views.algorithms.ITM import views_in_the_money_calculator
from views.restart import restart


def intro():
    print('ARKADIUS\nAuthor: Arkadiusz Jaworski\n\n')


def tools():
    print('Choose the financial tool to run\n')
    print('Press 1 for In The Money Algorithm')
    print('Press 2 for Black Scholes Merton Model Algorithm')
    return input('\nSelect: ')


def main():
    intro()
    tool = tools()

    if tool == '1':
        views_in_the_money_calculator()
    elif tool == '2':
        views_black_scholes_merton()
    else:
        restart('That option is invalid.', main)

if __name__ == '__main__':
    main()
