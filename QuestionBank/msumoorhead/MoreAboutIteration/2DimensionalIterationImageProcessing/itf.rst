.. activecode::  itf
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: MoreAboutIteration
    :subchapter: 2DimensionalIterationImageProcessing
    :topics: MoreAboutIteration/2DimensionalIterationImageProcessing
    :from_source: None
    :nocodelens:
    :timelimit: 30000

    import image, time

    img = image.Image("cs.png")
    win = image.ImageWin(img.getWidth(), img.getHeight())
    img.draw(win)
    print('making negative')
    time.sleep(1) # wait 1 second


    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)

            newred = 255 - p.getRed()
            newgreen = 255 - p.getGreen()
            newblue = 255 - p.getBlue()

            newpixel = image.Pixel(newred, newgreen, newblue)

            img.setPixel(col, row, newpixel)

    img.draw(win)
    print('display negative')
    time.sleep(5) # wait 5 seconds
    print('display original?')
    img.draw(win) # draw original image