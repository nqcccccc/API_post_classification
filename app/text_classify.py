import numpy as np

def classify(text,model):
    pred = model.predict(text,k=-1)

    label = pred[0]
    score = pred[1]

    arr_label = []
    for i in range(len(score)):
        if score[i] >= 0.7:
            arr_label.append(label[i].replace('__label__',''))

    if len(arr_label) == 0:
        arr_label.append(label[np.argmax(score)].replace('__label__',''))

    return arr_label

