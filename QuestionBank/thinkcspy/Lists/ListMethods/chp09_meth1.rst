.. activecode:: chp09_meth1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Lists
    :subchapter: ListMethods
    :topics: Lists/ListMethods
    :from_source: T
    :pct_on_first: 0.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 7.0

    mylist = []
    mylist.append(5)
    mylist.append(27)
    mylist.append(3)
    mylist.append(12)
    print(mylist)
    
    mylist.insert(1, 12)
    print(mylist)
    print(mylist.count(12))
    
    print(mylist.index(3))
    print(mylist.count(5))
    
    mylist.reverse()
    print(mylist)
    
    mylist.sort()
    print(mylist)
    
    mylist.remove(5)
    print(mylist)
    
    lastitem = mylist.pop()
    print(lastitem)
    print(mylist)