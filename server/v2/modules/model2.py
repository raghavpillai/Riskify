import pandas as pd
import numpy as np
import os
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM, Dropout, SimpleRNN, Embedding, Reshape
from keras.utils import to_categorical
from keras import regularizers
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


def readData():
    # Get labels from the labels.txt file
    data = np.array(
        [
            340.30756277,
            173.88151584,
            232.11530758,
            179.39840137,
            230.42959256,
            392.10498806,
            315.48157787,
            277.01662595,
            317.47378653,
            236.86595901,
            279.77506872,
            399.1543418,
            311.34391372,
            171.27631989,
            332.64522175,
            182.00359732,
            359.00367486,
            180.47112911,
            364.36731357,
            321.15171022,
            356.70497255,
            235.33349081,
            282.68675831,
            267.05558263,
            261.23220345,
            344.2919801,
            355.17250435,
            350.57509974,
            267.82181673,
            210.35425909,
            388.73355801,
            309.81144551,
            369.8841991,
            231.19582666,
            285.44520107,
            382.45043837,
            277.78286005,
            216.94387236,
            196.56204525,
            334.63743042,
            330.19327262,
            235.79323127,
            217.250366,
            194.41658977,
            361.6088708,
            283.29974559,
            258.16726705,
            348.88938471,
            223.9932261,
            206.06334812,
            239.62440178,
            355.32575117,
            208.51529724,
            363.60107947,
            245.90752141,
            329.12054488,
            393.1777158,
            266.90233581,
            284.21922651,
            223.68673246,
            205.9101013,
            331.41924719,
            185.83476783,
            315.94131833,
            192.27113428,
            381.22446381,
            340.76730323,
            252.03739423,
            350.88159338,
            269.04779129,
            336.32314544,
            256.94129248,
            347.05042287,
            236.71271219,
            223.83997928,
            175.56723086,
            387.50758345,
            255.40882428,
            242.53609137,
            370.80368003,
            394.55693718,
            353.94652978,
            272.1127277,
            292.03481435,
            385.51537478,
            209.43477816,
            240.08414224,
            172.04255399,
            175.26073722,
            397.00888631,
            385.82186842,
            239.7776486,
            231.65556712,
            298.16468716,
            204.22438627,
            374.48160371,
            315.02183741,
            245.75427459,
            311.956901,
        ]
    )
    labels = []
    for i in range(1, len(labels)):
        labels.append(i)
    data = to_categorical(labels)
    labels = np.array(data)
    return data, labels


print("Reading data...")
data, labels = readData()

print("Splitting Data")
data_train, data_test, labels_train, labels_test = train_test_split(
    data, labels
)

print("Building Model...")
# Create model
model = Sequential()
## LSTM / RNN goes here ##
model.add(Dense(3, activation="softmax"))

model.compile(
    loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"]
)

print("Training NN...")
history = model.fit(
    data_train,
    labels_train,
    epochs=1000,
    batch_size=50,
    validation_split=0.25,
    verbose=2,
)

results = model.evaluate(data_test, labels_test)

predictions = model.predict(data_test)

print(predictions[0].shape)
print(np.sum(predictions[0]))
print(np.argmax(predictions[0]))

print(results)

acc = history.history["acc"]
val_acc = history.history["val_acc"]
epochs = range(1, len(acc) + 1)
