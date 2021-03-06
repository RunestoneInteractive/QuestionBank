.. activecode:: Edge_Detection
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPImageDecisions
    :subchapter: imageIfElse
    :topics: CSPImageDecisions/imageIfElse
    :from_source: T
    :tour_1: "Structural Tour";  1: id2b-line1; 4: id2b-line4; 7-8: id2b-line7-8; 9: id2b-line9; 10: id2b-line10; 11-13: id2b-line11-13; 14: id2b-line14; 15-17: id2b-line15-17; 18: id2b-line18; 21-22: id2b-line21-22; 23-24: id2b-line23-24; 27: id2b-line27; 30-31: id2b-line29-30;
    :nocodelens:

    from image import *

    # CREATE AN IMAGE FROM A FILE
    img = Image("swan.jpg")

    # LOOP THROUGH ALL BUT LAST COLUMN
    for x in range(img.getWidth() - 1):
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
            if abs(average2 - average1) > 10:
                newPixel = Pixel(0, 0, 0)
            else:
                newPixel = Pixel(255, 255, 255)

            # CHANGE THE IMAGE
            img.setPixel(x, y, newPixel)

    # SHOW THE CHANGED IMAGE
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)