.. codelens:: clens7_8_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Conditionals
    :subchapter: Nestedconditionals
    :topics: Conditionals/Nestedconditionals
    :from_source: T
    :python: py3
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