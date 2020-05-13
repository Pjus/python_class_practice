import backtrader as bt


if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(1337.0)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())


    data = bt.feeds.YahooFinanceCSVData(dataname='AAPL',
                                  fromdate=datetime(2017, 1, 1),
                                  todate=datetime(2017, 12, 31))