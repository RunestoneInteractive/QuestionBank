.. activecode::  ch11ex18a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatImages
    :subchapter: ch11_exercises
    :topics: CSPRepeatImages/ch11_exercises
    :from_source: T
    :nocodelens:

            from image import *

            img = Image("vangogh.jpg")

            for x in range(int(img.getWidth()):
                for y in range(int(img.getHeight()/2)):

                    p = img.getPixel(x, y)
                    r = p.getRed()
                    g = p.getGreen()
                    b = p.getBlue()

                    newPixel = Pixel(r, g, b)
                    img.setPixel(x, y + int(img.getHeight()/2), newPixel)

    win = ImageWin(img.getWidth(),img.getHeight())
            img.draw(win)