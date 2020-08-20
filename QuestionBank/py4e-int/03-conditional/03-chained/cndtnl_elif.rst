.. codelens:: cndtnl_elif
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-chained
    :topics: 03-conditional/03-chained
    :from_source: T
    :showoutput:

    x = 12
    y = 12.0
    if x < y:
        print('x is less than y')
    elif x > y:
        print('x is greater than y')
    else:
        print('x and y are equal')
    print('All done.')