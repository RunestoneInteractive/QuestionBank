.. activecode:: Image_Negate_Quarter
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatImages
    :subchapter: changeData
    :topics: CSPRepeatImages/changeData
    :from_source: T
    :tour_1: "Important Lines Tour"; 1-2: imgR2-line1-2; 4-5: imgR2-line4-5; 8: imgR6-line8; 9: imgR6-line9; 10: imgR6-line10; 11: imgR6-line11; 13-17: imgR6-line13-17; 19-20: imgR6-line19-20; 22-23: imgR6-line22-23; 25-27: imgR6-line25-27;
    :nocodelens:

    # STEP 1: USE THE IMAGE LIBRARY
    from image import *

    # STEP 2: PICK THE IMAGE
    img = Image("vangogh.jpg")

    # STEP 3: SELECT THE DATA
    halfWidth = (int) (img.getWidth() / 2)
    halfHeight = (int) (img.getHeight() / 2)
    for x in range(halfWidth):
        for y in range(halfHeight):

            # STEP 4: GET THE DATA
            p = img.getPixel(x, y)
            r = p.getRed()
            g = p.getGreen()
            b = p.getBlue()

            # STEP 5: CREATE THE COLOR
            newPixel = Pixel(255-r, 255-g, 255-b)

            # STEP 6: CHANGE THE PIXEL
            img.setPixel(x, y, newPixel)

    # STEP 7: SHOW THE RESULT
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)