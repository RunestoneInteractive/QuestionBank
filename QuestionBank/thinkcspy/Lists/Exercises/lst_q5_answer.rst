.. activecode:: lst_q5_answer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Lists
    :subchapter: Exercises
    :topics: Lists/Exercises
    :from_source: T

    import random

    def max(lst):
        max = 0
        for e in lst:
            if e > max:
                max = e
        return max

    lst = []
    for i in range(100):
        lst.append(random.randint(0, 1000))

    print(max(lst))