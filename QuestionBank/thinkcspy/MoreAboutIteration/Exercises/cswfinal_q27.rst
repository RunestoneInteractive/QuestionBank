.. parsonsprob:: cswfinal_q27
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: MoreAboutIteration
   :subchapter: Exercises
   :topics: MoreAboutIteration/Exercises
   :from_source: F
   :pct_on_first: 0.2051282051
   :total_students_attempting: 39
   :num_students_correct: 32.0
   :mean_clicks_to_correct: 4.21875

   27. Put the following statements in order to brighten an image
   -----
   def modify(img):
   '''Returns a brightened copy of img'''
   =====
       target = img.clone()
   =====
       for y in range(target.getHeight()):
           for x in range(target.getWidth()):
   =====
               p = target.getPixel(x, y)
   =====
               r = p.getRed() + 100
               g = p.getGreen() + 100
               b = p.getBlue() + 100
   =====
               if r > 255:
                   r = 255
               if g > 255:
                   g = 255
               if b > 255:
                   b = 255
   =====
               target.setPixel(x, y, image.Pixel(r, g, b))
   =====
       return target