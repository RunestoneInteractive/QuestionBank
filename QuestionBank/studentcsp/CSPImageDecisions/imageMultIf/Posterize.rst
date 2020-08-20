.. activecode:: Posterize
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPImageDecisions
    :subchapter: imageMultIf
    :topics: CSPImageDecisions/imageMultIf
    :from_source: T
    :tour_1: "Structural Tour"; 1: id3-line1; 4: id3-line4; 7-8: id3-line7-8; 9: id3-line9; 11-13: id3-line11-13; 16-17: id3-line16-17; 18-19: id3-line18-19; 20-21: id3-line20-21; 22-23: id3-line22-23; 24-25: id3-line24-25; 26-27: id3-line26-27; 30: id3-line30; 33: id3-line33; 36-37: id3-line35-36;
    :nocodelens:

    from image import *

    # CREATE AN IMAGE FROM A FILE
    img = Image("arch.jpg")

    # LOOP THROUGH ALL PIXELS
    for x in range(img.getWidth()):
        for y in range(img.getHeight()):
            p = img.getPixel(x, y)

            r = p.getRed()
            g = p.getGreen()
            b = p.getBlue()

            # VALUES FOR THE NEW COLOR
            if r < 120:
                r = 0
            if r >= 120:
                r = 120
            if g < 120:
                g = 0
            if g >= 120:
                g = 120
            if b < 120:
                b = 0
            if b >= 120:
                b = 120

            # CREATE THE COLOR
            newPixel = Pixel(r,g,b)

            # CHANGE THE IMAGE
            img.setPixel(x, y, newPixel)

    # SHOW THE CHANGED IMAGE
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)