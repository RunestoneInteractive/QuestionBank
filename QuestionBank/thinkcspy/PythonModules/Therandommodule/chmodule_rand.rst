.. activecode:: chmodule_rand
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: PythonModules
    :subchapter: Therandommodule
    :topics: PythonModules/Therandommodule
    :from_source: T

    import random

    prob = random.random()
    print(prob)

    diceThrow = random.randrange(1, 7)       # return an int, one of 1,2,3,4,5,6
    print(diceThrow)