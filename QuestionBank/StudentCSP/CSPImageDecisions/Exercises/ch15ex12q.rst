.. activecode::  ch15ex12q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPImageDecisions
    :subchapter: Exercises
    :topics: CSPImageDecisions/Exercises
    :from_source: T
    :nocodelens:

    def edger(img):
        # LOOP THROUGH ALL BUT LAST COLUMN
        for x in range(img.getWidth() ):
            for y in range(img.getHeight()):
                p = img.getPixel(x, y)
                p2 = img.getPixel(x + 1, y)
                r1 = p.getRed()
                g1 = p.getGreen()
                b1 = p.getBlue()
                average1 = (r1 + g1 + b1) / 3
                r2 = p2.getRed()
                g2 = p2.getGreen()
                b2 = p2.getBlue()
                average2 = (r2 + g2 + b2) / 3

                # VALUES FOR THE NEW COLOR
                if abs(average2 - average1) > 10
                    newPixel = Pixel(0, 0, 0)
                else:
                    newPixel = Pixel(255, 255, 255)

                # CHANGE THE IMAGE
                img.setPixel(x, y, newPixel)

                # SHOW THE CHANGED IMAGE
                win = ImageWin(img.getWidth(),img.getHeight())
                img.draw(win)

        from image import *

        # CREATE AN IMAGE FROM A FILE
        img = Image(motorcycle.jpg)
        edger(img)