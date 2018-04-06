import ParsePhotoBB
from sklearn.neural_network import MLPClassifier

list = ParsePhotoBB.parse_photo_BW(r'..\Photos\dog\dogInChairFrame0.jpg')

clf = MLPClassifier()
clf.fit([list], ["Dog"])

print clf.predict(list)
