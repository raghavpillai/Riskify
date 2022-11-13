from keras import Model
from keras.layers import Input, Dense, Bidirectional
from keras.layers.recurrent import LSTM
import numpy as np

def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    return b, a # return x, y intercept

# def get_points(def_arr):
#     x = 0
#     x_arr = []
#     y_arr = []
#     for num in def_arr:
#         x_arr.append([x])
#         y_arr.append([num])
#         x += 1
#     data =

#     x_a = np.array(x_arr).reshape(-1,1)
#     y_a = np.array(y_arr).reshape(-1,1)


# def define_model():
#     input1 = Input(shape=(2,1)) #take the reshape last two values, see "data = np.reshape(data,(10,2,1))" which is "data/batch-size, row, column"
#     lstm1 = Bidirectional(LSTM(units=32))(input1)
#     dnn_hidden_layer1 = Dense(3, activation='relu')(lstm1)
#     dnn_output = Dense(1, activation='sigmoid')(dnn_hidden_layer1)
#     model = Model(inputs=[input1],outputs=[dnn_output])
#     # compile the model
#     model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#     model.summary()
#     return model

from keras import Model
from keras.layers import Input, Dense, Bidirectional
from keras.layers.recurrent import LSTM
import numpy as np

# define model for simple BI-LSTM + DNN based binary classifier
def define_model():
    input1 = Input(shape=(1,1)) #take the reshape last two values, see "data = np.reshape(data,(10,1,1))" which is "data/batch-size, row, column"
    lstm1 = Bidirectional(LSTM(units=32))(input1)
    dnn_hidden_layer1 = Dense(3, activation='relu')(lstm1)
    dnn_output = Dense(1, activation='sigmoid')(dnn_hidden_layer1)
    model = Model(inputs=[input1],outputs=[dnn_output])
    # compile the model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()
    return model
def get_points(def_arr):
# Take 1-D array data with 10 records/elements
    data = np.array([i for i in range(len(def_arr))])
    Y = def_arr #define the label for binary classification
    print("data = ", data)
    # Reshape the data to 3D-Numpy array
    data = np.reshape(data,(len(data),1,1))
    print("data after reshape => ",data)
    # Call the model
    model = define_model()
    # Fit the model
    model.fit([data],[np.array(Y)],epochs=4,batch_size=2,verbose=1)
    # Take a test data to test the working of the model
    test_data = np.array([[len(def_arr) + 1]])
    # reshape the test data
    test_data = np.reshape(test_data,(1,1,1))
    # predict the sigmoid output [0,1] for the 'test_data'
    pred = model.predict(test_data)
    print("predicted sigmoid output => ",pred)

l = [340.30756277,173.88151584,232.11530758,179.39840137,230.42959256,392.10498806,315.48157787,277.01662595,317.47378653,236.86595901,279.77506872,399.1543418,311.34391372,171.27631989,332.64522175,182.00359732,359.00367486,180.47112911,364.36731357,321.15171022,356.70497255,235.33349081,282.68675831,267.05558263,261.23220345,344.2919801,355.17250435,350.57509974,267.82181673,210.35425909,388.73355801,309.81144551,369.8841991,231.19582666,285.44520107,382.45043837,277.78286005,216.94387236,196.56204525,334.63743042,330.19327262,235.79323127,217.250366,194.41658977,361.6088708,283.29974559,258.16726705,348.88938471,223.9932261,206.06334812,239.62440178,355.32575117,208.51529724,363.60107947,245.90752141,329.12054488,393.1777158,266.90233581,284.21922651,223.68673246,205.9101013,331.41924719,185.83476783,315.94131833,192.27113428,381.22446381,340.76730323,252.03739423,350.88159338,269.04779129,336.32314544,256.94129248,347.05042287,236.71271219,223.83997928,175.56723086,387.50758345,255.40882428,242.53609137,370.80368003,394.55693718,353.94652978,272.1127277,292.03481435,385.51537478,209.43477816,240.08414224,172.04255399,175.26073722,397.00888631,385.82186842,239.7776486,231.65556712,298.16468716,204.22438627,374.48160371,315.02183741,245.75427459,311.956901]
get_points(l)
