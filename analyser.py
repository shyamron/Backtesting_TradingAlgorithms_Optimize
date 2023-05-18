from backtesting import Backtest, Strategy
from backtesting.lib import crossover,resample_apply
from backtesting.test import SMA
import yfinance as yf
import datetime as dt
from backtrader.analyzers import TradeAnalyzer
import talib


import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx



class SMAStrategy(Strategy):
    n1 = 10
    n2 = 20
    def init(self):
        price=self.data.Close
        self.ma1= self.I(SMA, price,self.n1)
        self.ma2= self.I(SMA, price,self.n2)

    def next(self):
        if crossover(self.ma1,self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()

class MACDStrategy(Strategy):
    def init(self):
        price=self.data.Close
        self.macd=self.I(lambda x:talib.MACD(x)[0],price)
        self.macd_signal=self.I(lambda x:talib.MACD(x)[1],price)
    def next(self):
        if crossover(self.macd, self.macd_signal):
            self.buy()
        elif crossover(self.macd_signal,self.macd):
            self.sell()

class RSIStrategy(Strategy):
    upper_bound = 70
    lower_bound = 30
    rsi_window = 14 
    
    def init(self):
        self.rsi = self.I(talib.RSI, self.data.Close, self.rsi_window)
    
    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()
        else:
            if crossover(self.lower_bound, self.rsi):
                self.buy()

def rsi_optimize(bt):
    stats=bt.optimize(
        upper_bound=range(50,85,5),
        lower_bound=range(10,45,5),
        rsi_window=range(10,30,2),
        maximize='Return [%]',
        constraint=lambda param: param.upper_bound > param.lower_bound
    )
    return stats

def macdoptimize(bt):
    pass

def sma_optimize(bt):
    stats = bt.optimize(n1=range(5, 30, 5),
                    n2=range(10, 70, 5),
                    maximize='Return [%]',
                    constraint=lambda param: param.n1 < param.n2)
    
    return stats

def optimize(backtest,entered_strategy):
    # if entered_strategy=='MACD':
    #   op_output=macdoptimize(backtest)
    if entered_strategy=='RSI':
       op_output=rsi_optimize(backtest)
    elif entered_strategy=='SMA':
       op_output= sma_optimize(backtest)
    else:
        print('no such strategy')
    return op_output

def analyse(entered_data):
    _start = dt.date(2022,1,2)
    _end = dt.date(2022,12,12)
    entered_ticker = entered_data['symbol']
    
    data = yf.download(entered_ticker, start = _start, end = _end)
    print(data)
    entered_strategy=entered_data['strategy']
    # if entered_strategy=='MACD':
        # backtest = Backtest(data, MACDStrategy, commission=0.002, exclusive_orders=True)
    if entered_strategy=='RSI':
        backtest=Backtest(data, RSIStrategy, commission=0.002, exclusive_orders=True)
    elif entered_strategy=='SMA':
        backtest=Backtest(data, SMAStrategy, commission=0.002, exclusive_orders=True)
    else:
        print('no such strategy')
    
    stats=backtest.run()
    final_plot=backtest.plot()
    print(stats)

    op_stats=optimize(backtest,entered_strategy)
    optimized_final_plot=backtest.plot()
    print(op_stats)
    final_output={
        'Start':stats.Start,
        'End':stats.End,
        'Equity_Final':stats['Equity Final [$]'],
        'Equity_Peak':stats['Equity Peak [$]'],
        'Return [%]': stats['Return [%]'],
        'Buy & Hold Return [%]': stats['Buy & Hold Return [%]']
    }
    
    optimised_final_output={
        'Equity_Final':op_stats['Equity Final [$]'],
        'Equity_Peak':op_stats['Equity Peak [$]'],
        'Return [%]': op_stats['Return [%]'],
        'Buy & Hold Return [%]': op_stats['Buy & Hold Return [%]']
    }
    return final_output,optimised_final_output
