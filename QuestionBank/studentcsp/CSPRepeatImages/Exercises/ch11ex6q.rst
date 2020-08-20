.. activecode::  ch11ex6q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPRepeatImages
    :subchapter: Exercises
    :topics: CSPRepeatImages/Exercises
    :from_source: T
    :nocodelens:

    # STEP 1: USE THE IMAGE LIBRARY
    from image import *
    # STEP 2: PICK THE IMAGE
    img = Image("swan.jpg")
    # STEP 3: LOOP THROUGH THE PIXELS
    pixels = img.getPixels()
    for
        # STEP 4: GET THE DATA
        b = p.get
        g = p.get
                r = p.get
        # STEP 5: MODIFY THE COLOR
        p.set
        # STEP 6: UPDATE THE IMAGE
        img.updatePixel(p)
    # STEP 7: SHOW THE RESULT
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)