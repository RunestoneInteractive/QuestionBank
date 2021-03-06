.. activecode:: act_code_hu_sepia_9
    :author: Sean Joyce
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: TransformingSequences
    :subchapter: Exercises
    :topics: TransformingSequences/Exercises
    :from_source: F

    In Chapter 9, your author describes how you can transform an image into "Sepia tone," by applying a formula.  I have provided that formula for you as a comment in the code window below; complete the pixel transformations necessary to apply such a Sepia tone filter to the given image.  **FOR FULL CREDIT**, also update the code so the transformation is visibly made *from the left edge of the image to the right edge,* instead of from the top down.
    ~~~~
    # CPS 201 - Spring, 2019

    # To transform an image using a Sepia tone filter
    # apply these formulas to each pixel (assuming a 
    # pixel's current RGB values are R, G, and B).
    # newR = (R * 0.393 + G * 0.769 + B * 0.189)
    # newG = (R * 0.349 + G * 0.686 + B * 0.168)
    # newB = (R * 0.272 + G * 0.534 + B * 0.131)

    import image

    # in this case, we load the image from a URL
    img = image.Image("https://runestone.academy/runestone/static/heidelberg_ac101s19/_static/GoldenGateBridgeCC.png")

    win = image.ImageWin(img.getWidth(), img.getHeight())
    img.draw(win)
    img.setDelay(1,15)   # setDelay(0) turns off animation

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)

            # your code here

    img.draw(win)
    win.exitonclick()