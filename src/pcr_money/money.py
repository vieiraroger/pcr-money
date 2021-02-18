
class Money():

    def __init__(self, value=0.0, decimals=2, coin_name='U$', method='round'):
        self.decimals = decimals
        self.coin_name = coin_name
        self.value = self.handle_value(value, decimals, method)


    @staticmethod
    def handle_value(value, decimals, method='round'):
        """
        TODO think a better way to select and do this method
        :method can be 'round' and 'truncation'
        """
        if(method == 'round'):
            return round(value, decimals)
        elif(method == 'truncation'):
            multiplier = pow(10, decimals)
            value_int = int(value * multiplier)
            return float(value_int/multiplier)


    def __str__(self):
        return self.coin_name + str(self.money)


    def __repr__(self):
        return f"<Money {self.value}>"
