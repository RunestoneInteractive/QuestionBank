.. activecode:: Nested_Loop_Clear_Red
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatImages
    :subchapter: changeColorLoc
    :topics: CSPRepeatImages/changeColorLoc
    :from_source: T
    :tour_1: "Important Lines Tour"; 2: nli1-line2; 5: nli1-line5; 8: nli1-line8; 9: nli1-line9; 12: nli1-line12; 15: nli1-line15; 18: nli1-line18; 21-22: nli1-line21-22;
    :nocodelens:

    # STEP 1: USE THE IMAGE LIBRARY
    from image import *

    # STEP 2: PICK THE IMAGE
    img = Image("vangogh.jpg")

    # STEP 3: LOOP THROUGH THE PIXELS
    for x in range(img.getWidth()):
        for y in range(img.getHeight()):

            # STEP 4: GET THE DATA
            p = img.getPixel(x, y)

            # STEP 5: MODIFY THE COLOR
            p.setRed(0)

            # STEP 6: MODIFY THE IMAGE
            img.updatePixel(p)

    # STEP 7: SHOW THE RESULT
    win = ImageWin(img.getWidth(),img.getHeight())
    img.draw(win)