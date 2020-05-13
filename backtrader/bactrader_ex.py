import backtrader as bt

"""
class PandasData(feed.DataBase):
    '''
    The ``dataname`` parameter inherited from ``feed.DataBase`` is the pandas
    DataFrame
    '''

    params = (
        # Possible values for datetime (must always be present)
        #  None : datetime is the "index" in the Pandas Dataframe
        #  -1 : autodetect position or case-wise equal name
        #  >= 0 : numeric index to the colum in the pandas dataframe
        #  string : column name (as index) in the pandas dataframe
        ('datetime', None),

        # Possible values below:
        #  None : column not present
        #  -1 : autodetect position or case-wise equal name
        #  >= 0 : numeric index to the colum in the pandas dataframe
        #  string : column name (as index) in the pandas dataframe
        ('open', -1),
        ('high', -1),
        ('low', -1),
        ('close', -1),
        ('volume', -1),
        ('openinterest', -1),
    )
    
"""

class MyStrategy(bt.Strategy):

    def __init__(self):  # Initiation
        self.sma = btind.SimpleMovingAverage(period=15)  # Processing

    def next(self):  # Processing
        if self.sma > self.data.close:
            # Do something
            pass

        elif self.sma < self.data.close: # Post-processing
            # Do something else
            pass

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=20)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)


if __name__ == '__main__':
    cerebro = bt.Cerebro()
    
    cerebro.broker.setcash(1337.0)
    cerebro.broker.setcommission(commission=0.001)



    data = bt.feeds.YahooFinanceCSVData(dataname='AAPL.csv')
    cerebro.adddata(data)
    cerebro.addstrategy(SmaCross)
    cerebro.run()

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    
    print('Ending Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.plot()