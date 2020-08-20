.. activecode:: Image_Functions
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPNameNames
    :subchapter: imageLib
    :topics: CSPNameNames/imageLib
    :from_source: T
    :tour_1: "Important Lines Tour"; 1,4,7,11,15,18: timg2-line1_4_7_11_15_18; 2: timg2-line2; 5: timg2-line5; 8-9: timg2-line8-9; 12-13: timg2-line12-13; 16: timg2-line16; 19-20: timg2-line19-20;
    :nocodelens:

    # USE THE IMAGE LIBRARY
    from image import *

    # CREATE AN IMAGE FROM A FILE
    img = Image("arch.jpg")

    # LOOP THROUGH THE PIXELS
    pixels = img.getPixels()
    for p in pixels:

        # MODIFY THE PIXEL COLOR
        r = p.getRed()
        p.setRed(r * 0.5)

        # UPDATE THE IMAGE
        img.updatePixel(p)

    # SHOW THE RESULT
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)