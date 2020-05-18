import datetime
from tushare.pro.client import DataApi
from vitu.configuration import Config


class API(DataApi):
    """
    tushare暂停只支持获取week、daily、60min、15min
    """
    def get_data(self, exchange, symbol, freq, start_date, end_date):
        if freq in ['1d', 'daily', 'day', 'd']:
            freq = 'daily'
        return self.coinbar(exchange=exchange, symbol=symbol, freq=freq, start_date=start_date, end_date=end_date)

    def get_price(self, exchange=None, symbol=None, freq=None, date=None):
        """
        :param exchange: "binance"
        :param symbol: 'btcusdt'
        :param date: '2019-08-01'
        :return:  回测：上一bar close_price
        """
        if freq in ['1d', 'daily', 'day', 'd']:
            freq = 'daily'
        time_format = '%Y-%m-%d' if len(date) == 10 else '%Y-%m-%d %H:%M:%S'
        start_date = str(datetime.datetime.strptime(date, time_format) - datetime.timedelta(days=1))
        end_date = date
        # print(exchange, symbol, freq, start_date, end_date)
        df = self.coinbar(exchange=exchange, symbol=symbol, freq=freq, start_date=start_date, end_date=end_date) # ( ]
        return df['close'].tolist()[0]

def get_price(exchange, symbol, freq, date):
    price = API(Config.tushare_token()).get_price(exchange, symbol, freq, date)
    return price

def get_data(exchange, symbol, freq, start_date, end_date):
    date = API(Config.tushare_token()).get_data(exchange, symbol, freq, start_date, end_date)
    return date

if __name__ == '__main__':
    import pandas as pd
    pd.set_option('display.max_rows',None)             # 让行显示完
    pd.set_option('display.max_columns',None)          # 让列显示完
    pd.set_option('display.width',1000)                # 宽度最大显示1000列

    import time
    start = time.time()
    # price = get_price("binance", "ethusdt", '1d', "2019-09-24")
    # print(price)
    #
    # price = get_price("binance", "ethbtc", 'd', "2019-09-24")
    # print(price)
    #
    # price = get_price("binance", "btcusdt", 'd', "2019-09-24")
    # print(price)
    #
    # data = get_data("binance", "btcusdt", '15min', "2019-09-24", '2019-09-25')
    # print(data)
    #
    # data = get_data("binance", "btcusdt", '30min', "2019-09-24", '2019-09-25')
    # print(data)

    data = get_data("binance", "btcusdt", 'd', "2019-09-24", '2019-09-30 08:00:00')
    print(data)

    print(time.time()-start)


    # while True:
    #     price = API(Config.tushare_token()).get_price("binance", "btcusdt", "2019-09-24")
    #     print(price)
        # time.sleep(0.5)

























