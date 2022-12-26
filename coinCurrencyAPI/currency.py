from currency_converter import CurrencyConverter


# Currency Convert by country


class CurrencyData:
    c = CurrencyConverter()


    def __init__(self, coin):
        self.coin = coin


    def convertcoin(self):
        data = self.c.convert(1, f'{self.coin}', 'USD')
        return {
            'value': data,
            'code': self.coin
        }


