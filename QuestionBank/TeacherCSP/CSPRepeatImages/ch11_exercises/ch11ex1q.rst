.. activecode:: ch11ex1q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatImages
    :subchapter: ch11_exercises
    :topics: CSPRepeatImages/ch11_exercises
    :from_source: T
    :nocodelens:

    from image import

    # CREATE AN IMAGE FROM A FILE
    img = Image("gal2.jpg"

    # LOOP THROUGH THE PIXELS
    pixelList = img.getPixels()
    for p in pixelList:

        # SET THE RED TO 0
        p.setRed()

        # UPDATE THE IMAGE
        img.updatePixel()

    # SHOW THE RESULT
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)