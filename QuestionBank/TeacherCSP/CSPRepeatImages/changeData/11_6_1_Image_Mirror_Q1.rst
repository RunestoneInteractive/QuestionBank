.. mchoice:: 11_6_1_Image_Mirror_Q1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPRepeatImages
   :subchapter: changeData
   :topics: CSPRepeatImages/changeData
   :from_source: T
   :answer_a: img.setPixel(halfway - x, y, newPixel)
   :answer_b: img.setPixel(x - halfway, y, newPixel)
   :answer_c: img.setPixel(img.getWidth() - 1 - x, y, newPixel)
   :answer_d: img.setPixel(x - img.getWidth(), y, newPixel)
   :correct: c
   :feedback_a: It does mirror, but only the left half
   :feedback_b: This creates two copies of the left half
   :feedback_c: Yes, it looks like the woman is kissing herself
   :feedback_d: No, no effect.

   Try it: How would you mirror the image from left-to-right around a vertical line in the middle of the picture?  Try changing line 22 to these.  If you get it right it will look like the women is nose to nose with herself.