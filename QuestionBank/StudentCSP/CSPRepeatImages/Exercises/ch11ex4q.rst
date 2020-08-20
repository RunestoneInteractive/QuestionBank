.. activecode::  ch11ex4q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPRepeatImages
    :subchapter: Exercises
    :topics: CSPRepeatImages/Exercises
    :from_source: T
    :nocodelens:

    # STEP 1: USE THE IMAGE LIBRARY
    from image import *
    # STEP 2: PICK THE IMAGE
    img = Image("kitten")
    # STEP 3: LOOP THROUGH THE PIXELS
    pixels = img.getPixels()
    for p in pixel:
        # STEP 4: GET THE DATA
        r = p.getred()
        b = p.getGreen()
        g = p.getBlue()
        # STEP 5: MODIFY THE COLOR
        p.setRed(g)
        p.setGreen(b)
        p.setBlue(r)
        # STEP 6: UPDATE THE IMAGE
        img.updatePixel(p)
    # STEP 7: SHOW THE RESULT
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)