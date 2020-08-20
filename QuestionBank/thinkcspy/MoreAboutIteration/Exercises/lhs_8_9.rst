.. activecode:: lhs_8_9
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: Exercises
    :topics: MoreAboutIteration/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.135770235
    :total_students_attempting: 383
    :num_students_correct: 368.0
    :mean_clicks_to_correct: 7.1304347826

    Write a function ``convertToSepia(img, w, h)`` that converts an image to sepia tone. The function should
    create a new image of size w x h, convert the ``img`` to sepia tone, and write out the pixels into
    the new image.
    
    The function should **return** the new sepia tone image.
    
    Use the following as the formula to calculate the new RGB's for each pixel. **Remember** that the pixel
    RGB's must be integers.
    
    ::
    
      newR = (R * 0.393 + G * 0.769 + B * 0.189)
      newG = (R * 0.349 + G * 0.686 + B * 0.168)
      newB = (R * 0.272 + G * 0.534 + B * 0.131)
    
    ~~~~
    # Name:
    
    import image
    
    def convertToSepia(img, w, h):
        # Write you code here
    
    def makeImage(w, h):
        newImg = image.EmptyImage(w, h)
        rinit = 255
        ginit = 255
        binit = 0
        for col in range(w):
            r = rinit
            g = ginit
            b = binit
            for row in range(h):
                r = r - 4
                g = g - 2
                b = b + 2
                newpixel = image.Pixel(r, g, b)
                newImg.setPixel(col, row, newpixel)
            rinit = rinit - 3
            ginit = ginit - 2
            binit = binit + 2
        return newImg
    
    win = image.ImageWin()
    img = makeImage(30,50)
    img.draw(win)
    
    # change the image to sepia tone by calling your routine
    # draw the image onto the window
    ====
    import random
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def genRandImage(self, w, h, seed):
            random.seed(seed)
            newImg = image.EmptyImage(w, h)
            for col in range(w):
                for row in range(h):
                    r = random.randrange(0, 256)
                    g = random.randrange(0, 256)
                    b = random.randrange(0, 256)
                    newpixel = image.Pixel(r, g, b)
                    newImg.setPixel(col, row, newpixel)
            return newImg
                    
        def golden_Sepia(self, img, w, h):
            newimg = image.EmptyImage(w, h)
            for col in range(w):
                for row in range(h):
                    p = img.getPixel(col, row)
        
                    r = p.getRed()
                    g = p.getGreen()
                    b = p.getBlue()
                    newR = int(r * 0.393 + g * 0.769 + b * 0.189)
                    newG = int(r * 0.349 + g * 0.686 + b * 0.168)
                    newB = int(r * 0.272 + g * 0.534 + b * 0.131)
        
                    newpixel = image.Pixel(newR, newG, newB)
                    newimg.setPixel(col, row, newpixel)
    
            return newimg
        
        def cmpImage(self, i1, i2, col, row):
            count = 0
            for c in range(col):
                for r in range(row):
    
                    p = i1.getPixel(c, r)
                    r1 = p.getRed()
                    g1 = p.getGreen()
                    b1 = p.getBlue()
    
                    p = i2.getPixel(c, r)
                    r2 = p.getRed()
                    g2 = p.getGreen()
                    b2 = p.getBlue()  
    
                    if (r1 != r2) or (g1 != g2) or (b1 != b2):
                        count = count + 1
    
                    if count == 1:
                        print("First pixel miscompare at col:", c, "row:", r)
                        print("Expected RGB:", r2, g2, b2, "Your RGB:", r1, g1, b1)
    
            return(count)
    
        def testOne(self):
            print("Auto-testing...")
            w = 30
            h = 20
            i1 = self.genRandImage(w, h, 123)
            i2 = self.genRandImage(w, h, 123)
            i1 = convertToSepia(i1, w, h)
            i2 = self.golden_Sepia(i2, w, h)
            count = self.cmpImage(i1, i2, w, h)
            self.assertEqual(count, 0, "Comparing pixels")
    
    myTests().main()