.. codelens:: sel1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Selection
    :subchapter: Nestedconditionals
    :topics: Selection/Nestedconditionals
    :from_source: T
    :showoutput:

    x = 10
    y = 10

    if x < y:
        print("x is less than y")
    else:
        if x > y:
            print("x is greater than y")
        else:
            print("x and y must be equal")