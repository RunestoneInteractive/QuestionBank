.. activecode::  act_ip_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Projects
    :subchapter: image_processing
    :topics: Projects/image_processing
    :from_source: T
    :nocodelens:

    import image

    img = image.Image("golden_gate.png")
    win = image.ImageWin(img.getWidth(), img.getHeight())
    img.draw(win)
    img.setDelay(1,15)   # setDelay(1, 2000) will speed up a lot                      # img.setDelay(delay, number of pixels between delay)

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)

            gray_value = # your code here

            newred = # your code here
            newgreen =  # your code here
            newblue =  # your code here

            newpixel = image.Pixel(newred, newgreen, newblue)

            img.setPixel(col, row, newpixel)

    img.draw(win)
    win.exitonclick()