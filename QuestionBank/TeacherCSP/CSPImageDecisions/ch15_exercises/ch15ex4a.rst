.. activecode::  ch15ex4a
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
    img = Image("gal2.jpg")

    # LOOP THROUGH ALL PIXELS
    for x in range(img.getWidth()):
        for y in range(img.getHeight()):
            p = img.getPixel(x, y)
            r = p.getRed()
            g = p.getGreen()
            b = p.getBlue()

            # VALUES FOR THE NEW COLOR
            if r > 200 and g > 200 and b > 200:

                # CREATE THE COLOR
                newPixel = Pixel(100, 100, 100)

                # CHANGE THE IMAGE
                img.setPixel(x, y, newPixel)

    # SHOW THE CHANGED IMAGE
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)