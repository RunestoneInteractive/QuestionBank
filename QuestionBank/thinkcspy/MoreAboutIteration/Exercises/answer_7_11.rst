.. activecode:: answer_7_11
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: MoreAboutIteration
   :subchapter: Exercises
   :topics: MoreAboutIteration/Exercises
   :from_source: T
   :nocodelens:

   import image

   def double(oldimage):
       oldw = oldimage.getWidth()
       oldh = oldimage.getHeight()

       newim = image.EmptyImage(oldw * 2, oldh * 2)
       for row in range(oldh):
           for col in range(oldw):
               oldpixel = oldimage.getPixel(col, row)

               newim.setPixel(2*col, 2*row, oldpixel)
               newim.setPixel(2*col+1, 2*row, oldpixel)
               newim.setPixel(2*col, 2*row+1, oldpixel)
               newim.setPixel(2*col+1, 2*row+1, oldpixel)

       return newim

   img = image.Image("luther.jpg")
   win = image.ImageWin(img.getWidth()*2, img.getHeight()*2)

   bigimg = double(img)
   bigimg.draw(win)

   win.exitonclick()