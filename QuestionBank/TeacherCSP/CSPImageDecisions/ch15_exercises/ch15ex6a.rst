.. activecode::  ch15ex6a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPImageDecisions
    :subchapter: ch15_exercises
    :topics: CSPImageDecisions/ch15_exercises
    :from_source: T
    :nocodelens:

    from image import *

    # CREATE THE IMAGES
    img1 = Image("motorcycle.jpg")
    img2 = Image("beach.jpg")
    width1 = img1.getWidth()
    height1 = img1.getHeight()
    width2= img2.getWidth()
    height2 = img2.getHeight()
    maxWidth = min(width1,width2)
    maxHeight = min(height1,height2)

    # LOOP THROUGH THE PIXELS
    for x in range(maxWidth):
      for y in range(maxHeight):
        p1 = img1.getPixel(x, y)
        r1 = p1.getRed()
        g1 = p1.getGreen()
        b1 = p1.getBlue()

        # CHECK IF THE PIXEL ISN'T WHITE
        if r1 < 250 and g1 < 250 and b1 < 250:

          # COPY THE COLOR TO IMG2
          img2.setPixel(x, y, p1)

    # SHOW THE CHANGED IMAGE
    win = ImageWin(img2.getWidth(),img2.getHeight())
    img2.draw(win)