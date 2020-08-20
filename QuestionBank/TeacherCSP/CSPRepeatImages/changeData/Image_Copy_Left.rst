.. activecode:: Image_Copy_Left
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatImages
    :subchapter: changeData
    :topics: CSPRepeatImages/changeData
    :from_source: T
    :tour_1: "Important Lines Tour"; 1-2: imgR2-line1-2; 4-5: imgR2-line4-5; 8: imgR8-line8; 9: imgR8-line9; 10: imgR8-line10; 12-16: imgR8-line12-16; 18-19: imgR8-line18-19; 21-22: imgR8-line21-22; 24-26: imgR8-line24-26;
    :nocodelens:

    # STEP 1: USE THE IMAGE LIBRARY
    from image import *

    # STEP 2: PICK THE IMAGE
    img = Image("vangogh.jpg")

    # STEP 3: SELECT THE DATA
    halfway = (int) (img.getWidth() / 2)
    for x in range(halfway):
        for y in range(img.getHeight()):

            # STEP 4: GET THE DATA
            p = img.getPixel(x, y)
            r = p.getRed()
            g = p.getGreen()
            b = p.getBlue()

            # STEP 5: CREATE THE COLOR
            newPixel = Pixel(r, g, b)

            # STEP 6: CHANGE THE PIXEL
            img.setPixel(halfway + x, y, newPixel)

    # STEP 7: SHOW THE RESULT
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)