.. activecode::  ch15ex7q
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
     img1 = Image("gal1.jpg")
     img2 = Image(guy1.jpg")

     # LOOP THROUGH ALL THE PIXELS IN IMG1
     for x in range(img1.getWidth():
         for y in range(img1.getHeight())
             p1 = img1.getPixel(x, )
             r1 = p1.getRed()
             g1 = p1.getGreen()
             b1 = p1.getBlue()

             # CHECK IF THE PIXEL ISN'T WHITE
             if r1 < 250 and g1 < 250  b1 < 250:

                 # COPY THE COLOR TO IMG2
                 img2.setPixel(x, y, p1)

     # SHOW THE CHANGED IMAGE
     win = ImageWin(img2.getWidth(),img2.getHeight())
     img2.draw(win)