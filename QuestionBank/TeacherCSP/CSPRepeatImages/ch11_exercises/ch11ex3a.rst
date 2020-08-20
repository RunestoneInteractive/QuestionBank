.. activecode::  ch11ex3a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatImages
    :subchapter: ch11_exercises
    :topics: CSPRepeatImages/ch11_exercises
    :from_source: T
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