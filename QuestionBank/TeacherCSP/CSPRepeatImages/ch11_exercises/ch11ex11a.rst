.. activecode::  ch11ex11a
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
    img = Image("gal2.jpg")

    # LOOP THROUGH THE PIXELS
    for x in range(int(img.getWidth() / 2)):
        for y in range(img.getHeight()):

            # GET THE DATA
            p = img.getPixel(x, y)

            # SET THE RED TO 0
            p.setRed(0)

            # UPDATE THE IMAGE
            img.updatePixel(p)

    # SHOW THE RESULT
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)