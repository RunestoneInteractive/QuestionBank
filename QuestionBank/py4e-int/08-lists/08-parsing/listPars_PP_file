.. parsonsprob:: listPars_PP_file
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-parsing
    :topics: 08-lists/08-parsing
    :from_source: T
    :practice: T

    The following code should open a file and read through the lines, splitting them when a line starts
    with "Hello", then printing the second word in the line. Watch out for extra pieces of code and
    indentation.
    -----
    fhand = open('myFile.txt')
    =====
    for line in fhand:
    =====
    for line in myFile: #distractor
    =====
        line = line.rstrip() #remove trailing whitespace
    =====
        if not line.startswith('From '): continue #distractor
    =====
        if not line.startswith('Hello'): continue
    =====
        words = line.split()
    =====
        print(words[1])
    =====
        print(words[2]) #distractor