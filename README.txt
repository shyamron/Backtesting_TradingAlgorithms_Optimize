Algorithmic Trading Platform with Backtesting and Optimization
This is final project given by Coderush as a part of Genese Placement Program. The projects is to build a trading platform that allows users to Backtest and Optimize Trading Strategies.
Tools Used:
1. Python with Backtesting library
2. Flask Framework
3. Yahoo Finance API
4. HTML/CSS
5. JS

The trading strategies used in this project are:
1.  Simple Moving Average (SMA)
2. Relative Strength Index (RSI) oscillator
Optimization is done by varying parameter values in SMA and RSI.
Files:
1. static_file/frontend.html is frontpage UI
2. backend.py uses Flask framework.
       Run “flask –app backend run” 
3. backend.py calls analyse function from analyser.py file. 
4. analyser.py runs all backtesting and optimization and returns outputs to UI and displays plots for each.

To run app,
1. Install modules from requirements.txt
pip install -r requirements.txt
	python version- 3.9.16
2. Run Flask app
   flask –app backend run”

