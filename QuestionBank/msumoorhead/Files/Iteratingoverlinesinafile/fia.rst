.. activecode:: fia
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Files
    :subchapter: Iteratingoverlinesinafile
    :topics: Files/Iteratingoverlinesinafile
    :from_source: None
    :nocodelens:
    :available_files: qbdata.txt

    qbfile = open("qbdata.txt", "r")

    for aline in qbfile:
        values = aline.split()
        print('{} {} has a rating of {}'.format(values[0], values[1], values[10]))

    qbfile.close()