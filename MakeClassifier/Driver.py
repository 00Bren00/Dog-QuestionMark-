import ParsePhotoBB
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib

fullFeaturesList = [None]*( 917 + 976)
fullLabelsList = [None]*( 917 + 976)

index = 0

# for i in range(266):
#     notDog = ParsePhotoBB.parse_photo_BW(r"..\Photos\not-dog\cat\cat" + str(i) + ".jpg")
#     fullFeaturesList[index] = notDog
#     fullLabelsList[index]   = "Not Dog"
#     index += 1
#
#     #TODO get cats

print "Parsing chair"

for i in range(917):
    notDog = ParsePhotoBB.parse_photo_BW(r"..\Photos\not-dog\NoDogJustChair\dogNotInChairFrame" + str(i) + ".jpg")
    fullFeaturesList[index] = notDog
    fullLabelsList[index]   = "Not Dog"
    index += 1
    #TODO get dogNotInChair

print "parsing dog"

for i in range(976):
    dog = ParsePhotoBB.parse_photo_BW(r"..\Photos\dog\dogInChairFrame" + str(i) + ".jpg")
    fullFeaturesList[index] = dog
    fullLabelsList[index]   = "Dog"
    index += 1

    #todo get all dog photos

# dog = ParsePhotoBB.parse_photo_BW(r"..\Photos\dog\dogInChairFrame" + str(i) + ".jpg")
# notDog = ParsePhotoBB.parse_photo_BW(r"..\Photos\not-dog\dogNotInChairFrame" + str(i) + ".jpg")
#
# fullFeaturesList[index] = dog
# fullLabelsList[index]   = "Dog"
#
# index += 1
#
# fullFeaturesList[index] = notDog
# fullLabelsList[index]   = "notDog"
#
# index += 1

list = ParsePhotoBB.parse_photo_BW(r"..\Photos\changRes\dogInChairFrame0.jpg")
print "Fitting"
clf = MLPClassifier()
clf.fit(fullFeaturesList, fullLabelsList)

joblib.dump(clf, r'..\Classifiers\Dog_Neural_Net.pkl')

print clf.predict([list])

#im = Image.open(r'..\Photos\dog\dogInChairFrame0.jpg')
#im.save(r"..\Photos\changRes\dogInChairFrame0.jpg", dpi=(60, 60))
