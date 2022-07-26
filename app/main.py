from typing import Union
from fastapi import FastAPI,Form
from pydantic import BaseModel
import cv2

import fasttext

from app.text_preprocessing import pre_process
from app.text_classify import classify
from app.image_classify import text_or_not,img_classify
from app.ocr_vietnamese import text_extractor

import tensorflow as tf

class Item(BaseModel):
    content: Union[str, None] = None
    img_url: Union[str, None] = None

model = fasttext.load_model('./app/model/fasttext_textclassify.bin')
model_textornot = tf.keras.models.load_model('./app/model/textOrnotResNet50.h5')
model_img = tf.keras.models.load_model('./app/model/ImageClassifyResnet50.h5')

app = FastAPI()


@app.post('/post-classify')
async def classify_post(item: Item):
    text_label = []
    img_label = []

    if(item.content is not None):
        text = pre_process(item.content)
        if(len(text) > 0):
            text_label = classify(text, model)
    
    if(item.img_url is not None):
        if(text_or_not(item.img_url,model_textornot) == 'khong-chu'):
            img_label = img_classify(item.img_url,model_img)
        else:
            img_text = text_extractor(item.img_url)
            img_text = pre_process(img_text)
            if(len(img_text) > 0):
                img_label = classify(img_text, model)
                if(len(text) < len(img_text)):
                    text_label = img_label
            else:
                img_label = img_classify(item.img_url,model_img)

    if len(text_label) > 0:
        label = text_label
    else:
        label = img_label

    return {'label':label}



