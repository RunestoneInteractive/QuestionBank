.. activecode::  act_ip_2
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
    img.setDelay(1,15)   # setDelay(0) turns off animation

    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            p = img.getPixel(col, row)

            # your code here

    img.draw(win)
    win.exitonclick()