.. activecode:: IT105Resoures_ex_1_1a
    :author: jenkins
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: IT105Resources
    :subchapter: Exercises
    :topics: IT105Resources/Exercises
    :from_source: F

    import random

    def countEven(lst):
        even = 0
        for e in lst:
            if e % 2 == 0:
                even += 1
        return even

    # make a random list to test the function
    lst = []
    for i in range(100):
        lst.append(random.randint(0, 1000))

    print(countEven(lst))