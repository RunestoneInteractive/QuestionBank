.. activecode:: miter_q7_answer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: Exercises
    :topics: MoreAboutIteration/Exercises
    :from_source: T
    :nocodelens:

    import image

    img = image.Image("luther.jpg")
    newimg = image.EmptyImage(img.getWidth(), img.getHeight())
    win = image.ImageWin()

    for col in range(img.getWidth()):
        for row in range(img.getHeight()):
            p = img.getPixel(col, row)

            newred = 0
            green = p.getGreen()
            blue = p.getBlue()

            newpixel = image.Pixel(newred, green, blue)

            newimg.setPixel(col, row, newpixel)

    newimg.draw(win)
    win.exitonclick()