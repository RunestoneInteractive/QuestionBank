.. activecode::  ch11ex10a
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
    img = Image("baby.jpg")
    # STEP 3: LOOP THROUGH THE PIXELS
    for x in range(img.getWidth()):
                for y in range(img.getHeight()):
            # STEP 4: GET THE DATA
                    p = img.getPixel(x,y)
                    r = p.getRed()
            b = p.getBlue()
            g = p.getGreen()
            # STEP 5: MODIFY THE COLOR
            p.setRed(r/2)
            p.setGreen(g/2)
            p.setBlue(b/2)
            # STEP 6: UPDATE THE IMAGE
            img.updatePixel(p)
    # STEP 7: SHOW THE RESULT
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)