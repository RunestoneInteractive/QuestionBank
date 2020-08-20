.. activecode:: liw
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Lists
    :subchapter: NestedLists
    :topics: Lists/NestedLists
    :from_source: None

    nested = [['h','i'], [2.0, 5], [10, 20]]
    i = 2
    j = 1
    innerlist = nested[i]
    print(innerlist)
    item = innerlist[j]
    print(item)

    print(nested[i][j])