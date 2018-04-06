from PIL import Image


def parse_photo_rgb(filePath):
    im = Image.open(filePath)

    pixels = list(im.getdata())

    myList = []

    for pixel in pixels:
        for value in pixel:
            myList.append(value)

    return myList
