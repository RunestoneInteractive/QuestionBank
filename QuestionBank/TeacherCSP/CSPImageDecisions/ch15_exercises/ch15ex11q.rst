.. activecode::  ch15ex11q
     :author: bmiller
     :difficulty: 3.0
     :basecourse: TeacherCSP
     :chapter: CSPImageDecisions
     :subchapter: ch15_exercises
     :topics: CSPImageDecisions/ch15_exercises
     :from_source: T
     :nocodelens:

     from image import *

     # CREATE AN IMAGE FROM A FILE
     img = Image("beach.jpg")

     # LOOP THROUGH ALL PIXELS
     for x in range(img.getWidth()):
         for y in range(img.getHeight()):
             p = img.getPixel(x, y)

             r = p.getRed()
             g = p.getGreen()
             b = p.getBlue()

             # VALUES FOR THE NEW COLOR
             if r < 120:
                 r = 0
             if r >= 120:
                 r = 120
             if g < 120:
                 g = 0
             if g >= 120:
                 g = 120
             if b < 120:
                 b = 0
             if b >= 120:
                 b = 120

             # CREATE THE COLOR
             newPixel = Pixel(r,g,b)

             # CHANGE THE IMAGE
             img.setPixel(x, y, newPixel)

     # SHOW THE CHANGED IMAGE
     win = ImageWin(img.getWidth(),img.getHeight())
     img.draw(win)