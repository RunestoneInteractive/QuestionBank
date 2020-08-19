.. parsonsprob:: midtermCopyNonWhitePixels
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPPracticeQuestions
   :subchapter: Exercises
   :topics: CSPPracticeQuestions/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.1176470588
   :total_students_attempting: 85
   :num_students_correct: 64.0
   :mean_clicks_to_correct: 5.65625

   The code below is supposed to copy the pixels that are not close to the color white from img1 to img2.  Put the code in the correct order.
   -----
   from image import *
   =====
   # CREATE THE IMAGES
   img1 = Image("lady_tiny.png")
   img2 = Image("eiffel.jpg")
   =====
   # LOOP THROUGH ALL THE PIXELS IN IMG1
   for x in range(img1.getWidth()):
       for y in range(img1.getHeight()):
   =====
           p1 = img1.getPixel(x, y)
           r1 = p1.getRed()
           g1 = p1.getGreen()
           b1 = p1.getBlue()
   =====
           # CHECK IF THE PIXEL ISN'T WHITE
           if r1 < 250 and g1 < 250 and b1 < 250:
   =====
               # COPY THE COLOR TO IMG2
               img2.setPixel(x, y + 130, p1)
   =====
   # SHOW THE CHANGED IMAGE
   win = ImageWin(img2.getWidth(),img2.getHeight())
   img2.draw(win)
   
   
   fig values (conf.py):
   
   arsons_div_class - custom CSS class of the component's outermost div