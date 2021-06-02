from decimal import *

class Money():

    def __init__(self, value=0.0, decimals=2, coin_name='U$', method='round'):
        self.decimals = decimals
        self.coin_name = coin_name
        self.value = self.handle_value(value, decimals=2, method='round')


    @staticmethod
    def handle_value(value, decimals, method):
        _round_methods = {
            'round' : lambda value, decimals: round(value, decimals),
            'truncation': lambda value: int(value),
            'ceil' : lambda value: ROUND_CEILING(value),
            'floor' : lambda value: ROUND_FLOOR(value)
        }
        value = Decimal(str(value))
        return float(_round_methods[method](value, decimals))


    def applyRound(self, decimals, method='round'):
        self.decimals = decimals
        self.value = self.handle_value(self.value, decimals, method)


    def __str__(self):
        return self.coin_name + str(self.money)


    def __repr__(self):
        return f"<Money {self.value}>"
