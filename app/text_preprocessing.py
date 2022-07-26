import pandas as pd
import numpy as np
import re
from itertools import groupby

# Xóa emoji
def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)
#Loại bỏ spam : 
def spam(text) :
    sentence = []
    for word in text.split() :
        if len(word) < 6 :
           sentence.append(word) 
        else :
            word = " "    
    sentence=' '.join(word for word in sentence)
    return sentence

def elongated_remove(text):
    return ''.join(c for c, _ in groupby(text))

# xóa số trong câu
def clean_number_object(string: str, punctuations=r'''!+()-[]{};:'"\,<>./?@#$%^&~''') -> str:
    # Xóa số
    for x in string.lower(): 
        if x in punctuations: 
            string = string.replace(x, "") 
    return string

def pre_process(text):
    text = remove_emojis(text)
    text = clean_number_object(text)
    text = text.lower()
    text = spam(text)
    text = elongated_remove(text)
    return text