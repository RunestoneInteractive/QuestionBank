.. parsonsprob:: Image_Set_Red_Half_Blue
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPRepeatImages
   :subchapter: pattern
   :topics: CSPRepeatImages/pattern
   :from_source: T
   :numbered: left
   :adaptive:

   The program below should set all the red values to half the blue values.  Drag the needed code blocks below from the left to the right in the correct order with the correct indention. There may be extra blocks that are not needed in a correct solution.  Click on the *Check Me* button to check your solution.
   -----
   from image import *
   =====
   import * #paired
   =====
   img = Image("beach.jpg")
   =====
   img = image("beach.jpg) #paired
   =====
   pixels = img.getPixels()
   for p in pixels:
   =====
   pixels = Image.getPixels()
   for p in pixels: #paired
   =====
       p.setRed(p.getBlue() * 0.5)
   =====
       img.updatePixel(p)
   =====
   win = ImageWin(img.getWidth(),img.getHeight())
   img.draw(win)