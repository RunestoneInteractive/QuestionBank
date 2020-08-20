.. activecode:: lip
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Lists
    :subchapter: ListMethods
    :topics: Lists/ListMethods
    :from_source: None

    mylist = []
    mylist.append(5)
    mylist.append(27)
    mylist.append(3)
    mylist.append(12)
    print(mylist)
    yourlist = [9,1]
    mylist.extend(yourlist)
    print(mylist)

    mylist = mylist.sort()
    print(mylist)