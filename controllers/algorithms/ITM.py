from models.algorithms.ITM import models_itm
from models.validation import validate_digits, validate_menu_options
from views.restart import restart


def controllers_in_the_money_calculator():
    # Press 1 for Long Call
    # Press 2 for Long Put
    # Press 3 for Short Call
    # Press 4 for Short Put
    option_type = input(
        'Enter 1 for Long Call.\nEnter 2 for Long Put.\nEnter 3 for Short Call.\nEnter 4 for Short Put\nEnter an Option type: ')

    if validate_menu_options([1, 2, 3, 4], option_type):
        stock_price = input('Enter the market price of the underlying asset: ')
        if validate_digits(stock_price):
            strike_price = input('Enter the strike price of the options contract: ')
            if validate_digits(strike_price):
                return models_itm(option_type, stock_price, strike_price)
            else:
                restart('Strike price entered is incorrect.', controllers_in_the_money_calculator)
        else:
            restart('Stock price entered is incorrect.', controllers_in_the_money_calculator)
    else:
        restart('Option type entered is incorrect.', controllers_in_the_money_calculator)
