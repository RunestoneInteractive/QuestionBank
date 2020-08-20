.. activecode:: intro_8
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds
    :chapter: Introduction
    :subchapter: ControlStructures
    :topics: Introduction/ControlStructures
    :from_source: T
    :caption: Processing Each Character in a List of Strings

    wordlist = ['cat','dog','rabbit']
    letterlist = [ ]
    for aword in wordlist:
        for aletter in aword:
            letterlist.append(aletter)
    print(letterlist)