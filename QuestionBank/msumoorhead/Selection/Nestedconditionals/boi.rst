.. activecode:: boi
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Selection
    :subchapter: Nestedconditionals
    :topics: Selection/Nestedconditionals
    :from_source: None

    x = 10
    y = 10

    if x < y:
        print("x is less than y")
    else:
        if x > y:
            print("x is greater than y")
        else:
            print("x and y must be equal")

    print('this is always printed')