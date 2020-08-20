.. activecode:: file_ex_testa
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-writeCode
    :topics: 07-files/07-writeCode
    :from_source: T
    :nocodelens:
    :optional:

    f = open("studentdata.txt", "r")

    for aline in f:
        items = aline.split()
        if len(items[1:]) >= 6:
            print(items[0])

    f.close()