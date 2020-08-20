.. parsonsprob:: functRandom_pp_nums
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-randomnumbers
    :topics: 04-functions/04-randomnumbers
    :from_source: T
    :adaptive:
    :practice: T
    :numbered: left

    Construct a block of code that correctly generates a random number from the list
    called "nums", then prints it out. Watch out for extra pieces of code!
    -----
    import random
    =====
    nums = [1, 2, 4, 5, 6, 76, 12]
    =====
    nums = (1, 2, 4, 5, 6, 76, 12) #distractor
    =====
    choice = random.choice(nums)
    =====
    choice = random.choice("nums") #distractor
    =====
    choice = random.random(nums) #distractor
    =====
    choice = random.randint("nums") #distractor
    =====
    print(choice)