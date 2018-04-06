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

    pixelNum = 0
    for pixel in pixels:
        pixelNum += 1
        if not ((pixelNum %4) == 0):
            continue

        total = 0
        for value in pixel:
            total += value

        total /= 3

        myList.append(total)

    return myList

def change_resolution(filePath, newfilePath):
    im = Image.open(filePath)

    im.save(newfilePath, optimize=True,quality=95)
