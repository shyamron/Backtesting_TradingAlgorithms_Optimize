## Algorithmic Trading Platform with Backtesting and Optimization

This project is a trading platform that allows users to backtest and optimize trading strategies. It utilizes various tools and technologies such as Python, the Backtesting library, Flask framework, Yahoo Finance API, HTML/CSS, and JavaScript.


**Project Structure**

The project consists of several files and directories:

1. static_file/frontend.html: This file contains the frontpage UI for the trading platform.
2. backend.py: This file is the backend of the trading platform and uses the Flask framework. It handles the routing and communication with the frontend.
3. analyser.py: This file contains the logic for backtesting and optimization of trading strategies. It is called by the backend.py file to perform the analysis and return the results to      the frontend.
4. requirements.txt: This file lists the required Python modules and their versions.


**Running the App**

1. Install modules from requirements.txt

	pip install -r requirements.txt
	
python version- 3.9.16

2. Run Flask app

   flask –app backend run”
   
   
**Trading Strategies:**

The trading platform implements two trading strategies: Simple Moving Average (SMA) and Relative Strength Index (RSI) oscillator. These strategies can be backtested and optimized using the platform.


**Functionality**

The trading platform allows users to perform the following tasks:

1. Backtest Trading Strategies: Users can select a trading strategy (SMA or RSI) and configure the required parameters. The platform will then perform a backtest using historical data obtained from the Yahoo Finance API.

2. Optimization: Users can optimize the parameters of the selected trading strategy. The platform will vary the parameter values and evaluate the strategy's performance to find the optimal values.

3. Display Results: The platform will display the backtest results and optimization outputs to the user. This includes performance metrics, and visualization of the strategy's performance using plots.


