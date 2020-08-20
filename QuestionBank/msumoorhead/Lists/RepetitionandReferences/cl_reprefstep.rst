.. codelens:: cl_reprefstep
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Lists
    :subchapter: RepetitionandReferences
    :topics: Lists/RepetitionandReferences
    :from_source: None
    :showoutput:

    origlist = [45, 76, 34, 55]

    newlist = [origlist] * 3

    print(newlist)

    origlist[1] = 99

    print(newlist)