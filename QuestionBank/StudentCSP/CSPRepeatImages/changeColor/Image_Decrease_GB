.. parsonsprob:: Image_Decrease_GB
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPRepeatImages
   :subchapter: changeColor
   :topics: CSPRepeatImages/changeColor
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.4991394148
   :total_students_attempting: 581
   :num_students_correct: 542.0
   :mean_clicks_to_correct: 2.7103321033

   Another way to get a similar effect to increasing the red, is to decrease the green and blue.  Figure out how to do that in the program above and then use that information to drag the code blocks below from the left to the right in the correct order with the correct indention.
   -----
   from image import *
   =====
   img = Image("beach.jpg")
   =====
   pixels = img.getPixels()
   for p in pixels:
   =====
       g = p.getGreen()
       b = p.getBlue()
   =====
       p.setGreen(g * 0.75)
       p.setBlue(b * 0.75)
   =====
       img.updatePixel(p)
   =====
   win = ImageWin(img.getWidth(),img.getHeight())
   img.draw(win)