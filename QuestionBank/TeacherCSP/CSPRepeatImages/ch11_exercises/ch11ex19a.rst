.. activecode::  ch11ex19a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatImages
    :subchapter: ch11_exercises
    :topics: CSPRepeatImages/ch11_exercises
    :from_source: T
    :nocodelens:

    def mirrorLeftToRight(img):

        # loop through the pixels from 0 to half the width
        for x in range(int(img.getWidth() / 2)):
            for y in range(img.getHeight()):

                p = img.getPixel(x, y)
                img.setPixel(img.getWidth() - 1 - x, y, p)

    from image import *
    img = Image("vangogh.jpg")
    mirrorLeftToRight(img)
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)