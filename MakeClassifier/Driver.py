import ParsePhotoBB
from sklearn.neural_network import MLPClassifier
from PIL import Image

fullFeaturesList = [None]*20
fullLabelsList = [None]*20

index = 0

for i in range(10):
    dog = ParsePhotoBB.parse_photo_BW(r"..\Photos\dog\dogInChairFrame" + str(i) + ".jpg")
    notDog = ParsePhotoBB.parse_photo_BW(r"..\Photos\not-dog\dogNotInChairFrame" + str(i) + ".jpg")

    fullFeaturesList[index] = dog
    fullLabelsList[index]   = "Dog"

    index += 1

    fullFeaturesList[index] = notDog
    fullLabelsList[index]   = "notDog"

    index += 1

list = ParsePhotoBB.parse_photo_BW(r"..\Photos\not-dog\dogNotInChairFrame37.jpg")
clf = MLPClassifier()
clf.fit(fullFeaturesList, fullLabelsList)

print clf.predict([list])

#im = Image.open(r'..\Photos\dog\dogInChairFrame0.jpg')
#im.save(r"..\Photos\changRes\dogInChairFrame0.jpg", dpi=(60, 60))
