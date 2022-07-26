import cv2
import numpy as np
from urllib.request import Request, urlopen

def read_img_from_url(url):
    req = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    return img