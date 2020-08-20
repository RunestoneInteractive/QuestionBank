.. activecode:: act_0_anim
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Projects
    :subchapter: scaffolded_code
    :topics: Projects/scaffolded_code
    :from_source: T

    import image

    def process11(img):
        #get the height and width of the image
        width=img.getWidth()
        height=img.getHeight()
        for row in range(height):
            for col in range(width):
                p = img.getPixel(col, row)
                #What are the red, blue and green values for p?
                red_value = p.getRed()
                green_value = p.getGreen()
                blue_value = p.getBlue()
                if (red_value + green_value + blue_value)/3 >= 255/2:
                    newred = 255
                    newgreen = 255
                    newblue = 255
                else:
                    newred = 0
                    newgreen = 0
                    newblue = 0

                #set new pixel to new color values.
                newpixel = image.Pixel(newred, newgreen, newblue)

                img.setPixel(col, row, newpixel)
        # then draw the new images

    img = image.Image("LutherBellPic.jpg")
    img.setDelay(1,15)
    newwin=image.ImageWin(img.getWidth(),img.getHeight())
    img.draw(newwin)
    process11(img)