.. activecode:: Image_Every_Other
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPRepeatImages
    :subchapter: changeData
    :topics: CSPRepeatImages/changeData
    :from_source: T
    :tour_1: "Important Lines Tour"; 1-2: imgR2-line1-2; 4-5: imgR2-line4-5; 8: imgR7-line8; 9: imgR7-line9;  11-13: imgR7-line11-13; 15-16: imgR7-line15-16; 18-19: imgR7-line18-19; 21-23: imgR7-line21-23; 25-27:
    :nocodelens:

    # STEP 1: USE THE IMAGE LIBRARY
    from image import *

    # STEP 2: PICK THE IMAGE
    img = Image("vangogh.jpg")

    # STEP 3: SELECT THE DATA
    for x in range(0,img.getWidth(),2):
        for y in range(0,img.getHeight(),2):

            # STEP 4: GET THE DATA
            p = img.getPixel(x, y)
            r = p.getRed()

            # STEP 5: CREATE THE COLOR
            newPixel = Pixel(r, 255, 0)

            # STEP 6: CHANGE THE PIXEL
            img.setPixel(x, y, newPixel)

    # STEP 7: SHOW THE RESULT
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)