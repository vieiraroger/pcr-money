from requests import get
import math
from src.enum_method import MethodEnum

roundv = MethodEnum.round.name
truncation = MethodEnum.truncation.name
floor = MethodEnum.floor.name
ceil = MethodEnum.ceil.name


class Money:

    def __init__(self, value=0.0, decimals=2, coin_name='U$', method=roundv):
        self.decimals = decimals
        self.coin_name = coin_name
        self.value = self.handle_value(value, decimals, method)

    @staticmethod
    def handle_value(value, decimals, method=roundv):
        if method == roundv:
            return round(value, decimals)
        elif method == truncation or method == floor:
            multiplier = pow(10, decimals)
            value_int = int(value * multiplier)
            return float(value_int/multiplier)
        elif method == ceil:
            multiplier = pow(10, decimals)
            value_int = int(value * (10 * multiplier))

            if value_int % 10 != 0:
                value_int += 10
            value_int = int(value_int/10)
            return float(value_int/multiplier)
        else:
            return None

    def applyRound(self, decimals, method=roundv):
        self.decimals = decimals
        self.value = self.handle_value(self.value, decimals, method)

    def __add__(self, new):
        """
        Money + Money operation
        We always save all decimals because each money can have a different quantity of decimals and
        differents round methods, so after using the plus operation with maths he can use the method:
        applyRound(decimals, method)
        """
        if self.decimals < new.decimals:
            sum_decimals = new.decimals
        else:
            sum_decimals = self.decimals
        
        sum_value = self.value + new.value
        return Money(sum_value, sum_decimals)

    def __str__(self):
        return self.coin_name + str(self.money)

    def __repr__(self):
        return f"<Money {self.value}>"


class Currency(object):
    def __init__(self, API_PATH='https://economia.awesomeapi.com.br/last/'):
        self.API_PATH = API_PATH

    def converter(self, FROM: str, TO: str, qnt=1):
        self.FROM = FROM
        self.TO = TO
        self.qnt = qnt
        
        api = get(''.join([self.API_PATH, FROM, '-', TO]))
        r = api.status_code

        if r == 200:
            return float(api.json()[FROM+TO]['ask']) * qnt
        return str(api) + " This currency isn't registered in the API or doesn't exist."
