from models.algorithms.BSM import models_bsm
from models.timeConverter import convert_time
from models.validation import validate_digits, validate_menu_options
from views.restart import restart


def controllers_black_scholes_merton():
    stock_price = input('Enter the market price of the underlying asset. i.e. 400 for £400 \nMarket Price: ')
    if validate_digits(stock_price):
        strike_price = input('Enter the strike price of the options contract i.e. 405 for £405 \nStrike Price: ')
        if validate_digits(strike_price):
            rate = input('Enter the rate-free rate of return i.e. 5 for 5% \nRate of return: ')
            if validate_digits(rate):
                print('How would you like to measure the expiration for the options contract?')
                time = input(
                    'Press 1 for minutes.\nPress 2 for hours.\nPress 3 for days.\nPress 4 for weeks.\nPress 5 for months.\nPress 6 for years.\n')
                if validate_menu_options([1, 2, 3, 4, 5, 6], time):
                    duration = input('Enter the duration to expiration for the options contract: ')
                    if validate_digits(duration):
                        years = convert_time(int(time), int(duration))
                        volatility = input(
                            'Enter the volatility of the underlying asset i.e. 20 for 20% \nVolatility rate: ')
                        if validate_digits(volatility):
                            dividend = input(
                                'Enter the dividend yield of the underlying asset: i.e. 1 for 1% \nDividend rate: ')
                            if validate_digits(dividend):
                                bsm = models_bsm(int(stock_price), int(strike_price), int(rate) / 100, years,
                                                 int(volatility) / 100,
                                                 int(dividend) / 100)
                                print(f'Value of Call option returned by the model is: £{(round(bsm["call"], 2))}')
                                print(f'Value of Put option returned by the model is: £{(round(bsm["put"], 2))}')

                            else:
                                restart('Dividend entered is incorrect.', controllers_black_scholes_merton)
                        else:
                            restart('Volatility entered is incorrect.', controllers_black_scholes_merton)
                else:
                    restart('Time entered is incorrect.', controllers_black_scholes_merton)
            else:
                restart('Rate entered is incorrect.', controllers_black_scholes_merton)
        else:
            restart('Strike price entered is incorrect.', controllers_black_scholes_merton)
    else:
        restart('Stock price entered is incorrect.', controllers_black_scholes_merton)
