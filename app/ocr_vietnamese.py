import pytesseract
import cv2
from PIL import Image
from app.readimage import read_img_from_url


def Nguong1(img,T):
  g=img.copy()
  for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if(img[i][j]>T):
          g[i][j]=255
        else:
          g[i][j]=0
  return g


def Nguong2(img,T):
  g=img.copy()
  for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        if(img[i][j]<T):
          g[i][j]=255
        else:
          g[i][j]=0
  return g


def text_extractor(url):
    img = read_img_from_url(url)
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img1_nguong=Nguong1(img1,170)
    img1_nguong=Nguong2(img1_nguong,220)
    # pytesseract.pytesseract.tesseract_cmd = (
    #     r'/usr/bin/tesseract'
    # )
    text = pytesseract.image_to_string(img1_nguong, lang="vie")
    return text
