.. activecode:: lhs_8_8
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: Exercises
    :topics: MoreAboutIteration/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.106870229
    :total_students_attempting: 393
    :num_students_correct: 377.0
    :mean_clicks_to_correct: 13.8832891247

    Write a function ``grayScale(img, w, h)`` that converts an image to grayscale. The function should
    create a new image of size w x h, convert the ``img`` to grayscale and write out the pixels into
    the new image.
    
    The function should **return** the new grayscale image.
    
    **NOTE:** When doing the average of the RGB values, do an integer divide ``//`` rather than a floating point divde.
    
    ~~~~
    # Name:
    
    import image
    
    def grayScale(img, w, h):
        # Write your code here
    
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
    
    # make a window and image for testing purposes
    win = image.ImageWin()
    img = makeImage(30,50)
    img.draw(win)
    
    # change the image to gray scale by calling your routine
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
                    
        def golden_grayScale(self, img, w, h):
            newimg = image.EmptyImage(w, h)
            for col in range(w):
                for row in range(h):
                    p = img.getPixel(col, row)
        
                    red = p.getRed()
                    green = p.getGreen()
                    blue = p.getBlue()
        
                    gs = (red + green + blue) // 3
        
                    newpixel = image.Pixel(gs, gs, gs)
        
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
            w = 10
            h = 20
            i1 = self.genRandImage(w, h, 123)
            i2 = self.genRandImage(w, h, 123)
            i1 = grayScale(i1, w, h)
            i2 = self.golden_grayScale(i2, w, h)
            count = self.cmpImage(i1, i2, w, h)
            self.assertEqual(count, 0, "Comparing pixels")
    
    myTests().main()