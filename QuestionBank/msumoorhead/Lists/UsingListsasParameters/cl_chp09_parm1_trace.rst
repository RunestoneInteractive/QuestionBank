.. codelens:: cl_chp09_parm1_trace
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Lists
    :subchapter: UsingListsasParameters
    :topics: Lists/UsingListsasParameters
    :from_source: None

    def doubleStuff(aList):
        """ Overwrite each element in aList with double its value. """
        for position in range(len(aList)):
            aList[position] = 2 * aList[position]

    things = [2, 5, 9]

    doubleStuff(things)