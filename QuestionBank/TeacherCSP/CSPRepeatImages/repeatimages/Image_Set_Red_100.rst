.. parsonsprob:: Image_Set_Red_100
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPRepeatImages
   :subchapter: repeatimages
   :topics: CSPRepeatImages/repeatimages
   :from_source: T
   :numbered: left
   :adaptive:

   The program below should set all the red values to 100.  Drag the needed code blocks below from the left to the right in the correct order with the correct indention. There may be extra blocks that are not needed in a correct solution.  Click on the *Check Me* button to check your solution.
   -----
   from image import *
   =====
   from Image import * #paired
   =====
   img = Image("arch.jpg")
   =====
   img = image("arch.jpg") #paired
   =====
   pixels = img.getPixels()
   for p in pixels:
   =====
   pixels = img.getPixels
   for p in pixels: #paired
   =====
       p.setRed(100)
   =====
       p.set(100) #paired
   =====
       img.updatePixel(p)
   =====
   win = ImageWin(img.getWidth(),img.getHeight())
   img.draw(win)