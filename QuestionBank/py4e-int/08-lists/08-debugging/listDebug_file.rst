.. activecode:: listDebug_file
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-debugging
    :topics: 08-lists/08-debugging
    :from_source: T
    :available_files: mboxShort1

    fhand = open('mboxShort1.txt')
    count = 0
    for line in fhand:
        words = line.split()
        # print 'Debug:', words
        if len(words) == 0 : continue
        if words[0] != 'From' : continue
        print(words[2])