.. activecode::  ch11ex14a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatImages
    :subchapter: ch11_exercises
    :topics: CSPRepeatImages/ch11_exercises
    :from_source: T
    :nocodelens:

    from image import *
    # CREATE AN IMAGE FROM A FILE
            img = Image("guy1.jpg")
    # LOOP THROUGH THE PIXELS
            for x in range(0, int(img.getWidth()), 5):
                for y in range(0, img.getHeight(), 5):
        # GET THE DATA
                p = img.getPixel(x, y)
        # SET THE PIXEL
                p.setGreen(0)
                p.setBlue(0)
        # UPDATE THE IMAGE
                img.updatePixel(p)
    # SHOW THE RESULT
        win = ImageWin(img.getWidth(),img.getHeight())
        img.draw(win)