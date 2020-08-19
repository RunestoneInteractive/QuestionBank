.. activecode::  ch11ex2q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPRepeatImages
    :subchapter: Exercises
    :topics: CSPRepeatImages/Exercises
    :from_source: T
    :nocodelens:

    # USE THE IMAGE LIBRARY
    from image import *
    # PICK THE IMAGE
    img = Image("puppy.jpg")
    # LOOP THROUGH THE PIXELS
    pixelList = img.getPixels()
    for p in pixelList:
        # SET THE COLOR
        p.setRed(0)
        # UPDATE THE PIXEL
        img.updatePixel(p)

    # SHOW THE RESULT
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)