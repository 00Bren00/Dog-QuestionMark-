import ParsePhotoBB
from sklearn.neural_network import MLPClassifier
from PIL import Image

list = ParsePhotoBB.parse_photo_BW(r"..\Photos\changRes\dogInChairFrame0.jpg")
clf = MLPClassifier()
clf.fit([list], ["Dog"])

print clf.predict([list])

#im = Image.open(r'..\Photos\dog\dogInChairFrame0.jpg')
#im.save(r"..\Photos\changRes\dogInChairFrame0.jpg", dpi=(60, 60))
