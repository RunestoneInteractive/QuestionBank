.. activecode:: ch07_table1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: SimpleTables
    :topics: MoreAboutIteration/SimpleTables
    :from_source: T
    :nocodelens:

    print("n", '\t', "2**n")     #table column headings
    print("---", '\t', "-----")

    for x in range(13):        # generate values for columns
        print(x, '\t', 2 ** x)