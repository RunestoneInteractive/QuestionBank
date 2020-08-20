.. parsonsprob:: str-mixed-time
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-MixedupCode
    :topics: 06-strings/06-MixedupCode
    :from_source: T
    :adaptive:
    :numbered: left
    :practice: T
    :noindent:

    The following program segment should print the phrase, "It takes us 2 hours and 45 minutes to get home from camp.". But, the blocks have been mixed up and include an extra block that isn't correct.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
    -----
    numHours = 2
    numMinutes = 45.0
    =====
    print("It takes us " + str(numHours) + " hours and " + str(numMinutes) + " minutes to get home from camp.")
    =====
    print("It takes us " + numHours + " hours and " + numMinutes + " minutes to get home from camp.") #paired