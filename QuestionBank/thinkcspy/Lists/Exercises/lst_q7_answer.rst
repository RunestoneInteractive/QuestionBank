.. activecode:: lst_q7_answer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Lists
    :subchapter: Exercises
    :topics: Lists/Exercises
    :from_source: T

    import random

    def countOdd(lst):
        odd = 0
        for e in lst:
            if e % 2 != 0:
                odd = odd + 1
        return odd

    # make a random list to test the function
    lst = []
    for i in range(100):
        lst.append(random.randint(0, 1000))

    print(countOdd(lst))