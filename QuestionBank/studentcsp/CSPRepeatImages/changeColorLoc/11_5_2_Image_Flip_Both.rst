.. activecode:: 11_5_2_Image_Flip_Both
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPRepeatImages
    :subchapter: changeColorLoc
    :topics: CSPRepeatImages/changeColorLoc
    :from_source: T
    :tour_1: "Important Lines Tour"; 8-9: nli3-line8-9; 12: nli3-line12; 15: nli3-line15;
    :nocodelens:

    # STEP 1: USE THE IMAGE LIBRARY
    from image import *

    # STEP 2: PICK THE IMAGE
    img = Image("vangogh.jpg")

    # STEP 3: SELECT THE DATA
    for x in range(img.getWidth()):
        for y in range(img.getHeight()):

            # STEP 4: GET THE DATA
            p = img.getPixel(x, y)

            # STEP 6: CHANGE THE IMAGE
            img.setPixel(img.getWidth() - 1 - x,
                         img.getHeight() - 1 - y,
                         p)

    # STEP 7: SHOW THE RESULT
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)