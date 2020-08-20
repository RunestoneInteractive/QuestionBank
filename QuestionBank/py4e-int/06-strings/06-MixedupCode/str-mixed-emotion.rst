.. parsonsprob:: str-mixed-emotion
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

    The following segment should print the statement, "So happy 4 you!". The blocks have been mixed up, and include two extra blocks that are not correct.  Drag the blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
    -----
    emotion = "So happy "
    =====
    emotion = "So happy ' #distractor
    =====
    print(emotion + 4 + " you!") #distractor
    =====
    print(emotion + str(4) + " you!")