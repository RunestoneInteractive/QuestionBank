.. activecode::  itd
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: MoreAboutIteration
    :subchapter: 2DimensionalIterationImageProcessing
    :topics: MoreAboutIteration/2DimensionalIterationImageProcessing
    :from_source: None
    :nocodelens:

    import image
    img = image.Image("annefan.png")

    print(img.getWidth())
    print(img.getHeight())

    p = img.getPixel(45, 55)
    print(p.getRed(), p.getGreen(), p.getBlue())