.. activecode::  ch11ex15a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatImages
    :subchapter: ch11_exercises
    :topics: CSPRepeatImages/ch11_exercises
    :from_source: T
    :nocodelens:

    def keepOnlyGreen(img):

        # loop through all the pixels
        pixels = img.getPixels();
        for p in pixels:

            p.setRed(0)
            p.setBlue(0)

            # change the pixel color at the current location
            img.updatePixel(p)

    from image import *
    img = Image("beach.jpg")
    keepOnlyGreen(img)
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)