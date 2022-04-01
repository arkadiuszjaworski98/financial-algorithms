from views.intro import views_intro
from controllers.algorithms.ITM import controllers_in_the_money_calculator


def views_in_the_money_calculator():
    views_intro('In The Money (ITM) Calculator', controllers_in_the_money_calculator)