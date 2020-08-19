.. mchoice:: cswfinal_q29
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: MoreAboutIteration
   :subchapter: Exercises
   :topics: MoreAboutIteration/Exercises
   :from_source: F
   :answer_a: Converts an image to grayscale
   :answer_b: Creates an image that is entirely green
   :answer_c: Brightens an image
   :answer_d: Darkens an image
   :correct: a
   :random: 
   :pct_on_first: 0.5128205128
   :total_students_attempting: 39
   :num_students_correct: 37.0
   :mean_clicks_to_correct: 1.8108108108

   29. What does the following function do? You may use IDLE to run it. If you do that, you'll have to write some supporting code (probably in a main() function) to get an image, pass it to process(), and show it. Don't forget to call main(), and to import cImage as image. cImage.py can be found on trace in the Programs\Chapter8 folder; you can also find some images there and example programs to look at.::
   
      def process(img):
          target = img.clone()
          for y in range(target.getHeight()):
              for x in range(target.getWidth()):
                  p = target.getPixel(x, y)
                  value = p.getGreen()
                  c = image.Pixel(value, value, value)
                  target.setPixel(x, y, c)
          return target