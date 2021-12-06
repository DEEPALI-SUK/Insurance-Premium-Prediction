import pickle
import numpy as np

__model = None

def get_expense(age,bmi,children,gender,smoke,location):
    x = np.zeros(11)
    x[0] = age
    x[1] = bmi
    x[2] = children
    print(x[1])
    if gender=='female':
        x[3] = 1
        x[4] = 0
    else:
        x[3] = 0
        x[4] = 1
    print(smoke)
    if smoke=='smoke_yes':
        x[5] = 0
        x[6] = 1
    else:
        x[5] = 1
        x[6] = 0

    if location=='northeast':
        x[7] = 1
        x[8] = 0
        x[9] = 0
        x[10] = 0
    elif location=='northwest':
        x[7] = 0
        x[8] = 1
        x[9] = 0
        x[10] = 0
    elif location=='southeast':
        x[7] = 0
        x[8] = 0
        x[9] = 1
        x[10] = 0
    else:
        x[7] = 0
        x[8] = 0
        x[9] = 0
        x[10] = 1
    for i in x:
        print(i)

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __model
    if __model is None:
        with open('./artifacts/insurance_premium_prediction_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    #print(get_expense(19,27.9,0,'female','smoke_yes','southwest'))

