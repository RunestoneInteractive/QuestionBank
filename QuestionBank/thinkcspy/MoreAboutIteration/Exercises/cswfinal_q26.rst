.. parsonsprob:: cswfinal_q26
   :author: Lloyd Smith
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: MoreAboutIteration
   :subchapter: Exercises
   :topics: MoreAboutIteration/Exercises
   :from_source: F
   :pct_on_first: 0.0512820513
   :total_students_attempting: 39
   :num_students_correct: 28.0
   :mean_clicks_to_correct: 11.0

   26. Put the following lines of code in order to implement a function that returns an image that preserves all the black cats from img; all non-black pixels will be set to white. thr is a threshold used to measure how close a pixel is to black and distance measures the distance between the colors of two pixels.
   -----
   def black_cats(img, black, white, thr):
   '''
   Returns an image that preserves black cats in img
   black and white are black and white pixels; thr is an integer
   '''
   =====
       new_img = img.clone()
   =====
       for y in range(img.getHeight()):
           for x in range(img.getWidth()):
   =====
               p = img.getPixel(x, y)
   =====
               dist = distance(p, black)
   =====
               if dist > thr:
   =====
                   p = white
   =====
               new_img.setPixel(x, y, p)
   =====
       return new_img
   =====