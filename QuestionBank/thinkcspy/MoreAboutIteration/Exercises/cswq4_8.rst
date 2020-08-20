.. parsonsprob:: cswq4_8
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: MoreAboutIteration
   :subchapter: Exercises
   :topics: MoreAboutIteration/Exercises
   :from_source: F
   :pct_on_first: 0.0
   :total_students_attempting: 6
   :num_students_correct: 4.0
   :mean_clicks_to_correct: 10.25

   Drag the following instructions into the right order to create a function that returns a darkened copy of an image.
   -----
   import cImage as image
   =====
   def darken(img):
   '''Returns a darkened copy of img'''
   =====
        copy = img.clone()
   =====
        for y in range(copy.getHeight()):
            for x in range(copy.getWidth()):
   =====
                p = copy.getPixel(x, y)
   =====
                r = int(p.getRed() * 0.7)
                g = int(p.getGreen() * 0.7)
                b = int(p.getBlue() * 0.7)
   =====
                new_p = image.Pixel(r, g, b)
   =====
                copy.setPixel(x, y, new_p)
   =====
        return copy