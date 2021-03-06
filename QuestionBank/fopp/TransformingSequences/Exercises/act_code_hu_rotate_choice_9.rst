.. activecode:: act_code_hu_rotate_choice_9
    :author: Sean Joyce
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: TransformingSequences
    :subchapter: Exercises
    :topics: TransformingSequences/Exercises
    :from_source: F

    In the Chapter 9 project, we have worked on various image transformations.  I have provided some template code for you below that loads in one of your author's standard images from the textbook. Complete a program that prompts the user to enter an integer, describing their choice of rotation. An input of 0 signifies 90 degrees clockwise; an input of 1 signifies 90 degrees counterclockwise.  Your program should display both the original image and the (properly) rotated new image.
    ~~~~
    import image

    # INSERT CODE HERE that prompts the user to enter 
    # an integer, indicating their choice for rotation
    # 0 = 90 degrees clockwise; 
    # 1 = 90 degrees counterclockwise)

    # Here, I set up the "original" image and 
    # drawing window for you
    img = image.Image('https://runestone.academy/runestone/static/heidelberg_ac101s19/_static/GoldenGateBridgeCC.png')
    width = img.getWidth()
    height = img.getHeight()

    # make the window big enough to hold both 
    # the original image and the rotated image
    win = image.ImageWin(width + height, height + width)
    img.draw(win)

    # INSERT CODE HERE to rotate the image properly,
    # based on the user's choice - don't forget to start
    # with a new, empty Image object of the right size

    # finally, I include the code below to draw your
    # new image below the  old image on window
    # you should not need to change this
    newImg.draw(win, 0.5, height)