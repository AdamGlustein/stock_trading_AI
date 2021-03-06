import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.model_selection import train_test_split

## TODO: move real-time section to a update file/function. In main block, iterate over columns names (stock names), grab specific data using pandas, then process. 
## TODO: include TA lib data processing to include desired indicators as well as pool past data. 

def processData(fileName):
    df = pd.read_csv(fileName)
    df['G/B Buy'] = 1 or 0 ## TODO: insert calculation to decide. 
    ## TODO: insert more changes
    return df

def buildBuyModel(trainData, testData, trainLabels, testLabels):
    model = models.Sequential([ ## toggle dropout layers to see change in performance. 
        layers.Dense(64, activation='relu', input_shape=len(testData.keys())),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(1, activation='softmax') ## possible is layers.Softmax(dtype='float64')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metric=['accuracy'])
    model.fit(trainData, trainLabels, epochs=30)
    model.evaluate(testData, testLabels)
    return model

if __name__ == "__main__":
    filename = 'GenZ'
    data = processData(filename)
    train_data = data.sample(frac=0.8, random_state=0)
    test_data = data.drop(train_data.index)
    train_label = train_data.pop('G/B Buy')    ## if this does not work surround in []
    test_label = test_data.pop('G/B Buy')
    sellmodel = buildSellModel(train_data, test_data, train_label, test_label)
    output = sellmodel.predict[## add all current info here]
    if output > 0.95:
        print('Buy' + stock_name)
        print(output + 'confidence')
