.. mchoice:: cswfinal_q31
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: MoreAboutIteration
   :subchapter: Exercises
   :topics: MoreAboutIteration/Exercises
   :from_source: F
   :answer_a: Returns a new image that has the top half of img1 and the bottom half of img2
   :answer_b: Returns a brightened image
   :answer_c: Returns an image with a horizontal green line drawn across the midpoint
   :answer_d: Returns an image with pixels randomly chosen from img1 and img2
   :correct: a
   :random: 
   :pct_on_first: 0.775
   :total_students_attempting: 40
   :num_students_correct: 39.0
   :mean_clicks_to_correct: 1.358974359

   31. What does the following code do? Assume img1 and img2 are two images that are the same size. You may run the function.::
   
      def do_something(img1, img2):
          w = img1.getWidth()
          h = img1.getHeight()
          new_img = img1.clone()
          for y in range(0, int(h/2)):
              for x in range(0, w):
                  p = img1.getPixel(x, y)
                  new_img.setPixel(x, y, p)
          for y in range(int(h/2), h):
              for x in range(0, w):
                  p = img2.getPixel(x, y)
                  new_img.setPixel(x, y, p)
          return new_img