.. activecode::  ch15ex15a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPImageDecisions
    :subchapter: ch15_exercises
    :topics: CSPImageDecisions/ch15_exercises
    :from_source: T
    :nocodelens:

    from image import *

    # CREATE AN IMAGE FROM A FILE
    img = Image("beach.jpg")

    # LOOP THROUGH ALL PIXELS
    for x in range(img.getWidth()):
        for y in range(img.getHeight()):
            p = img.getPixel(x, y)

            r = p.getRed()
            g = p.getGreen()
            b = p.getBlue()

            # VALUES FOR THE NEW COLOR
            if r < 85:
                r = 0
            elif r < 170:
                r = 85
            else:
                r = 170
            if g < 85:
                g = 0
            elif g < 170:
                g = 85
            else:
                g = 170
            if b < 85:
                b = 0
            elif b < 170:
                b = 85
            else:
                b = 170

            # CREATE THE COLOR
            newPixel = Pixel(r,g,b)

            # CHANGE THE IMAGE
            img.setPixel(x, y, newPixel)

    # SHOW THE CHANGED IMAGE
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)