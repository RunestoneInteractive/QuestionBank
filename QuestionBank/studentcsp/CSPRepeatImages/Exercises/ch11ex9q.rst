.. activecode::  ch11ex9q
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
     img = Image("beach.jpg")

     # STEP 3: LOOP THROUGH THE PIXELS
     pixels = img.getPixels();
     for p in pixels:

         p.setGreen(g * 0)
         p.setBlue(b * 0)
         g = p.getGreen()
         b = p.getBlue()

         # STEP 6: UPDATE THE IMAGE
         img.updatePixel(p)

     # STEP 7: SHOW THE RESULT
     win = ImageWin(img.getWidth(),img.getHeight())
     img.draw(win)