.. activecode:: Color_Replace
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPImageDecisions
    :subchapter: decImages
    :topics: CSPImageDecisions/decImages
    :from_source: T
    :tour_1: "Structural Tour"; 1: id1-line1; 4: id1-line4; 7-8: id1-line7-8; 9: id1-line9; 10-12: id1-line10-12; 15: id1-line15; 18: id1-line18; 21: id1-line21; 24-25: id1-line23-24;
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
            if r > 200 and g < 100 and b < 100:

                # CREATE THE COLOR
                newPixel = Pixel(0, g, b)

                # CHANGE THE IMAGE
                img.setPixel(x, y, newPixel)

    # SHOW THE CHANGED IMAGE
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)