.. activecode:: act_0_learnfuncs
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Projects
    :subchapter: scaffolded_code
    :topics: Projects/scaffolded_code
    :from_source: T
    :include: act_0_imageproc
    :nocodelens:

    # Here is seed text that can go in the activecode window for them to modify
    original = image.Image('yawning_squirrel.jpg')
    final = process10(original)
    newwin=image.ImageWin(final.getWidth(),final.getHeight())
    final.draw(newwin)