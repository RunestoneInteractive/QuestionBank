.. activecode:: Image_Pattern
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPRepeatImages
    :subchapter: pattern
    :topics: CSPRepeatImages/pattern
    :from_source: T
    :tour_1: "Important Lines Tour"; 2: timg4-line2; 5: timg4-line5; 8-9: timg4-line8-9; 12-14: timg4-line12-14; 17-19: timg4-line17-19; 22: timg4-line22; 25-26: timg4-line25-26;
    :nocodelens:

    # STEP 1: USE THE IMAGE LIBRARY
    from image import *

    # STEP 2: PICK THE IMAGE
    img = Image("beach.jpg")

    # STEP 3: LOOP THROUGH THE PIXELS
    pixels = img.getPixels()
    for p in pixels:

        # STEP 4: GET THE DATA
        r = p.getRed()
        g = p.getGreen()
        b = p.getBlue()

        # STEP 5: MODIFY THE COLOR
        p.setRed(g)
        p.setGreen(b)
        p.setBlue(r)

        # STEP 6: UPDATE THE IMAGE
        img.updatePixel(p)

    # STEP 7: SHOW THE RESULT
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)