import cv2
import numpy as np
from app.readimage import read_img_from_url

dict_class={
    0:'am-thuc', 
    1:'bat-dong-san', 
    2:'dong-thuc-vat', 
    3:'giai-tri', 
    4:'the-thao', 
    5:'thoi-trang', 
    6:'tri-thuc', 
    7:'xa-hoi'}

dict_class1={
    0:'co-chu', 
    1:'khong-chu'}

def text_or_not(url,model):
    image = read_img_from_url(url)
    image_resized= cv2.resize(image, (240,240))
    image=np.expand_dims(image_resized,axis=0)
    pred=model.predict(image)
    return dict_class1[np.argmax(pred)]

def img_classify(url,model):
    label_arr = []

    image = read_img_from_url(url)
    image_resized= cv2.resize(image, (240,240))
    image=np.expand_dims(image_resized,axis=0)
    pred=model.predict(image)
    for i,j in zip(np.ravel(np.argsort(pred)),np.sort(np.ravel(pred))):
        if j >= 0.8:
            label_arr.append(dict_class[i])
    if len(label_arr) == 0:
        label_arr.append(dict_class[np.argmax(pred)])
    return label_arr