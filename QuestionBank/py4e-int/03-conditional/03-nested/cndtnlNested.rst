.. codelens:: cndtnlNested
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-nested
    :topics: 03-conditional/03-nested
    :from_source: T

    x = 5
    y = 6
    if x == y:
        print('x and y are equal')
    else:
        if x < y:
            print('x is less than y')
        else:
            print('x is greater than y')
    print('All done.')