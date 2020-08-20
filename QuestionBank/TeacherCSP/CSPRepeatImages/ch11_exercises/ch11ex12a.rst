.. activecode::  ch11ex12a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatImages
    :subchapter: ch11_exercises
    :topics: CSPRepeatImages/ch11_exercises
    :from_source: T
    :nocodelens:

    from image import *
    # CREATE AN IMAGE FROM A FILE
    img = Image("vangogh.jpg")

    for x in range(int(img.getWidth()/2)):
        for y in range(int(img.getHeight() / 2), img.getHeight()):
            # GET THE DATA
            p = img.getPixel(x, y)
            # SET THE PIXEL
            p.setRed(0)
            p.setGreen(0)
            # UPDATE THE PIXEL
            img.updatePixel(p)
    # SHOW THE RESULT
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)