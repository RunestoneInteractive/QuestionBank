.. activecode::  ch11ex16a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatImages
    :subchapter: ch11_exercises
    :topics: CSPRepeatImages/ch11_exercises
    :from_source: T
    :nocodelens:

    from image import *

    img = Image("beach.jpg")

    for x in range(int(img.getWidth()/2)):
        for y in range(img.getHeight()):
            p = img.getPixel(x,y)

            r = p.getRed()
            g = p.getGreen()
            b = p.getBlue()
            avg = (r + g + b)/3

            p.setRed(avg)
            p.setGreen(avg)
            p.setBlue(avg)


            img.updatePixel(p)


    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)