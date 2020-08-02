# Stock Trading Neural Net Using Real-Time Indicators

This project is a neural net used to predict stock movement using technical analysis indicators such as RSI, VWAP, EMA and more. The indicators are accessed in real-time so the system can notify you when a stock triggers the "Buy" or "Sell" condition.

The model is tuned with various hyperparameters which the user can set before training. These are:
1. Trade interval: the time that you will hold the stock. The price change over the trade interval is used during supervised training of the model.
2. Threshold gain/loss: the percentage value that the stock must rise/fall in the trade interval to be classified as a "Buy" or "Sell" during training. These values can be set independently.
3. Training index: the index that the model uses to generate training data, defaulting to the S&P 500. 

After training, when using the model, the user also sets:
1. Stock indices: which indices the model analyzes. The default setting is the S&P 500, however we will soon add the NASDAQ, TSX and more.
2. Confidence level: the required model confidence to trigger a "Buy" or "Sell" notification. The default value is 95%.

The project is still under development and not yet trained or tested.




