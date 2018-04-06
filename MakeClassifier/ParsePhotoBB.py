from PIL import Image


def parse_photo_rgb(filePath):
    im = Image.open(filePath)

    pixels = list(im.getdata())

    myList = []

    for pixel in pixels:
        for value in pixel:
            myList.append(value)

    return myList

#BW is black and white
def parse_photo_BW(filePath):
    im = Image.open(filePath)

    pixels = list(im.getdata())

    myList = []

    for pixel in pixels:
        total = 0
        for value in pixel:
            total += value

        total /= 3

        myList.append(total)

    return myList
