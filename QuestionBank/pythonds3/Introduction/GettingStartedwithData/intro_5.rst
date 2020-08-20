.. activecode:: intro_5
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: Introduction
    :subchapter: GettingStartedwithData
    :topics: Introduction/GettingStartedwithData
    :from_source: T
    :caption: Examples of List Methods

    my_list = [1024, 3, True, 6.5]
    my_list.append(False)
    print(my_list)
    my_list.insert(2,4.5)
    print(my_list)
    print(my_list.pop())
    print(my_list)
    print(my_list.pop(1))
    print(my_list)
    my_list.pop(2)
    print(my_list)
    my_list.sort()
    print(my_list)
    my_list.reverse()
    print(my_list)
    print(my_list.count(6.5))
    print(my_list.index(4.5))
    my_list.remove(6.5)
    print(my_list)
    del my_list[0]
    print(my_list)