.. parsonsprob:: file_mixed_travel
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-mixedupCode
    :topics: 07-files/07-mixedupCode
    :from_source: T
    :numbered: left
    :adaptive:
    :practice: T

    The following program counts the number of characters in the file "travel_plans.txt", but
    the code is mixed up. Drag the blocks of statements from the left column to the right column
    and put them in the right order. Watch out for extra pieces of code and indentation!
    -----
    travelFile = open("travel_plans.txt", "r")
    =====
    travelFile = open("travel_plans.txt","w") #distractor
    =====
    num = 0
    =====
    num = 1 #paired
    =====
    for line in travelFile:
    =====
    for line in "travelFile": #paired
    =====
        lineCharacters = len(line)
    =====
        num = num + lineCharacters
    =====
    print(lineCharacters) #distractor
    =====
    print(num)