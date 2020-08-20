.. activecode::  ch15ex20a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPImageDecisions
    :subchapter: ch15_exercises
    :topics: CSPImageDecisions/ch15_exercises
    :from_source: T
    :nocodelens:

    from image import *

    def redToGray(aPic):
        img = Image(aPic)

        # LOOP THROUGH ALL PIXELS
        for x in range(img.getWidth()):
            for y in range(img.getHeight()):
                p = img.getPixel(x, y)
                r = p.getRed()
                g = p.getGreen()
                b = p.getBlue()
                avg = (r + g + b) / 3
                # VALUES FOR THE NEW COLOR
                if r > 200 and g < 100 and b < 100:

                    # CREATE THE COLOR
                    newPixel = Pixel(avg,avg,avg)

                    # CHANGE THE IMAGE
                    img.setPixel(x, y, newPixel)

        # SHOW THE CHANGED IMAGE
        win = ImageWin(img.getWidth(),img.getHeight())
        img.draw(win)

    redToGray("gal2.jpg")