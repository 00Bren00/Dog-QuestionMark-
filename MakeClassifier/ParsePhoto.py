from PIL import Image
from sklearn.neural_network import MLPClassifier
import cv2
import numpy as np
from matplotlib import pyplot as plt

def parsePhoto(path):
    photo = Image.open(path, 'r').convert('RGB')
    pix = photo.load()
    width, height = photo.size
    pixList = []
    for i in range(width):
        for j in range(height):
            for value in pix[i,j]:
                pixList.append(value)

    return pixList
    #return createPixelList(photo.load())

def createPixelList(photoData):
    print photoData[0]
    list = []
    for pixel in photoData:
        for value in pixel:
            list.append(value)

    return list


list = parsePhoto(r'C:\Users\remem\PycharmProjects\OpenCV\dog\dogInChairFrame0.jpg')
clf = MLPClassifier
clf = MLPClassifier.fit([list], ["Dog"])
#clf.fit([list], ["Dog"])

#print len(list)

