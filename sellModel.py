import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.model_selection import train_test_split


def buildSellModel(trainData, testData, trainLabels, testLabels):
    model = models.Sequential([ ## edit to fit needs. need to change input shape
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
