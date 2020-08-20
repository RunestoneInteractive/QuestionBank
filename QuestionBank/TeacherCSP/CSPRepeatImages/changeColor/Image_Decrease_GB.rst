.. parsonsprob:: Image_Decrease_GB
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPRepeatImages
   :subchapter: changeColor
   :topics: CSPRepeatImages/changeColor
   :from_source: T
   :numbered: left
   :adaptive:

   Another way to get a similar effect to increasing the red, is to decrease the green and blue by 25%.  Figure out how to do that in the program above and then use that information to drag the needed code blocks below from the left to the right in the correct order with the correct indention. There may be extra blocks that are not needed in a correct solution.  Click on the *Check Me* button to check your solution.
   -----
   from image import *
   =====
   img = Image("beach.jpg")
   =====
   img = image("beach.jpg") #paired
   =====
   pixels = img.getPixels()
   for p in pixels:
   =====
       g = p.getGreen()
       b = p.getBlue()
   =====
       g = p.getgreen()
       b = p.getblue() #paired
   =====
       p.setGreen(g * 0.75)
       p.setBlue(b * 0.75)
   =====
       p.setGreen(g * 0.25)
       p.setBlue(b * 0.25) #paired
   =====
       img.updatePixel(p)
   =====
   win = ImageWin(img.getWidth(),img.getHeight())
   img.draw(win)