.. activecode::  pixelex1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: 2DimensionalIterationImageProcessing
    :topics: MoreAboutIteration/2DimensionalIterationImageProcessing
    :from_source: T
    :nocodelens:

    import image
    img = image.Image("luther.jpg")

    print(img.getWidth())
    print(img.getHeight())

    p = img.getPixel(45, 55)
    print(p.getRed(), p.getGreen(), p.getBlue())