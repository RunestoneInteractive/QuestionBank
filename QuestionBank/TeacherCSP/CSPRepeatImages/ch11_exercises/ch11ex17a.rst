.. activecode::  ch11ex17a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatImages
    :subchapter: ch11_exercises
    :topics: CSPRepeatImages/ch11_exercises
    :from_source: T
    :nocodelens:

    def negate(img):

        # loop through all the pixels
        for x in range(img.getWidth()):
            for y in range(img.getHeight()):

                # get the red, green, and blue at the current pixel
                p = img.getPixel(x, y)
                r = p.getRed()
                g = p.getGreen()
                b = p.getBlue()

                # create a new pixel with the negated color
                newPixel = Pixel(255-r, 255-g, 255-b)

                # change the pixel color at the current location
                img.setPixel(x, y, newPixel)

    from image import *
    img = Image("vangogh.jpg")
    negate(img)
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)