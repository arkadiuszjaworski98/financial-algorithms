from controllers.algorithms.BSM import controllers_black_scholes_merton
from views.intro import views_intro


def views_black_scholes_merton():
    views_intro('Black Scholes Merton Model', controllers_black_scholes_merton)