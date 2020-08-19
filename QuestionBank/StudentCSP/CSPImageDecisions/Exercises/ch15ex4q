.. activecode::  ch15ex4q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPImageDecisions
    :subchapter: Exercises
    :topics: CSPImageDecisions/Exercises
    :from_source: T
    :nocodelens:

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
    if r > 0 and g > 0 and b > 0:

    # CREATE THE COLOR
    newPixel = Pixel(100, 100, 100)

    # CHANGE THE IMAGE
    img.setPixel(x, y, p)

    # SHOW THE CHANGED IMAGE
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)