.. activecode:: Image_Location_Change
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPRepeatImages
    :subchapter: changeColorLoc
    :topics: CSPRepeatImages/changeColorLoc
    :from_source: T
    :tour_1: "Important Lines Tour"; 2: nli2-line2; 5: nli2-line5; 8-9: nli2-line8-9; 12: nli2-line12; 15: nli2-line15; 18-19: nli2-line18-19;
    :nocodelens:

    # STEP 1: USE THE IMAGE LIBRARY
    from image import *

    # STEP 2: PICK THE IMAGE
    img = Image("vangogh.jpg")

    # STEP 3: LOOP THROUGH THE PIXELS
    last = min(img.getWidth(), img.getHeight())
    for x in range(last):
        for y in range(last):

            # STEP 4: GET THE DATA
            p = img.getPixel(x, y)

            # STEP 6: MODIFY THE IMAGE
            img.setPixel(y, x, p)

    # STEP 7: SHOW THE RESULT
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)