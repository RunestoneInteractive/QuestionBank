.. activecode:: listDebug_ac_print
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-debugging
    :topics: 08-lists/08-debugging
    :from_source: T
    :caption: Revisiting file access.

    fhand = open('mboxShort1.txt')
    for line in fhand:
        words = line.split()
        if words[0] != 'From' : continue
        print(words[2])