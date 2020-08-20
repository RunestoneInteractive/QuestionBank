.. activecode:: intro_5
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds
    :chapter: Introduction
    :subchapter: GettingStartedwithData
    :topics: Introduction/GettingStartedwithData
    :from_source: T
    :caption: Examples of List Methods

    myList = [1024, 3, True, 6.5]
    myList.append(False)
    print(myList)
    myList.insert(2,4.5)
    print(myList)
    print(myList.pop())
    print(myList)
    print(myList.pop(1))
    print(myList)
    myList.pop(2)
    print(myList)
    myList.sort()
    print(myList)
    myList.reverse()
    print(myList)
    print(myList.count(6.5))
    print(myList.index(4.5))
    myList.remove(6.5)
    print(myList)
    del myList[0]
    print(myList)