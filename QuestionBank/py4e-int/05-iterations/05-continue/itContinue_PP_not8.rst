.. parsonsprob:: itContinue_PP_not8
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 05-iterations
    :subchapter: 05-continue
    :topics: 05-iterations/05-continue
    :from_source: T
    :numbered: left
    :practice: T
    :adaptive:

    Construct a block of code that prints the numbers 1 through 10, but skips the number 8.
    The loop will start by incrementing n, before doing anything else. Look out for extra code pieces
    and watch your indentation!
    -----
    n = 0
    =====
    n = 1 #distractor
    =====
    while (n < 10):
    =====
    while (n < 10) #distractor
    =====
    while (n <= 10): #distractor
    =====
        n = n + 1
    =====
        if n == 8:
    =====
            continue
    =====
        print(n)