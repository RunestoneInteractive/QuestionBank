.. activecode::  ch15ex2q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPImageDecisions
    :subchapter: Exercises
    :topics: CSPImageDecisions/Exercises
    :from_source: T
    :nocodelens:

    from image import *

    # CREATE AN IMAGE FROM A FILE
    img = Image("girl.jpg")

    # LOOP THROUGH ALL PIXELS
    for x in range(img.getWidth()):
    for y in range(img.getHeight()):
            p = img.getPixel(x, y)
            r = p.getRed()
            g = p.getGreen()
            b = p.getBlue()

            # VALUES FOR THE NEW COLOR
            if r < 150 and g > 100 and b > 100:

                # CREATE THE COLOR
                newPixel = Pixel(0, 0, 0)

                # CHANGE THE IMAGE
                img.setPixel(x, y, newPixel)

    # SHOW THE CHANGED IMAGE
        win = ImageWin(img.getWidth(),img.getHeight())
        img.draw(win)