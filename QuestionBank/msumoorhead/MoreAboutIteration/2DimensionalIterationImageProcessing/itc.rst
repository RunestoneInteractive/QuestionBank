.. activecode::  itc
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: MoreAboutIteration
    :subchapter: 2DimensionalIterationImageProcessing
    :topics: MoreAboutIteration/2DimensionalIterationImageProcessing
    :from_source: None
    :nocodelens:

    import image

    p = image.Pixel(45, 76, 200)
    print(p.getRed())
    p.setRed(66)
    print(p.getRed())
    p.setBlue(p.getGreen())
    print(p.getGreen(), p.getBlue())