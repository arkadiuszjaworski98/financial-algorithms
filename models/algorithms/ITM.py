def models_itm(option_type, stock_price, strike_price):
    if option_type is None or stock_price is None or strike_price is None:
        return False

    if option_type == '1':  # Long Call
        if stock_price > strike_price:
            return print('The Long Call option is in-the-money.')
        elif stock_price < strike_price:
            return print('The Long Call option is out-of-the-money.')
        elif stock_price == strike_price:
            return print('The Long Call option is at-the-money.')
    elif option_type == '2':  # Long Put
        if stock_price > strike_price:
            return print('The Long Put option is out-of-the-money.')
        elif stock_price < strike_price:
            return print('The Long Put option is in-the-money.')
        elif stock_price == strike_price:
            return print('The Long Put option is at-the-money.')
    elif option_type == '3':  # Short Call
        if stock_price > strike_price:
            return print('The Short Call option is out-of-the-money.')
        elif stock_price < strike_price:
            return print('The Short Call option is in-the-money.')
        elif stock_price == strike_price:
            return print('The Short Call option is at-the-money.')
    elif option_type == '4':  # Short Put
        if stock_price > strike_price:
            return print('The Short Put option is in-the-money.')
        elif stock_price < strike_price:
            return print('The Short Put option is out-of-the-money.')
        elif stock_price == strike_price:
            return print('The Short Put option is at-the-money.')
    else:
        return False
