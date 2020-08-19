.. parsonsprob:: mixedupcode_question11_10
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 11-regex
    :subchapter: 11-mixedupcode
    :topics: 11-regex/11-mixedupcode
    :from_source: T
    :numbered: left
    :practice: T
    :adaptive:

    The following code should search for lines that start with 'X' followed by any
    non whitespace characters and ':' followed by a space and any number (that can be a float)
    then print the number if it is greater than zero. The blocks have been mixed up, and include
    two extra blocks that are not correct. Watch out for the extra blocks and indentation!
    -----
    import re
    =====
    hand = open('mbox-short.txt')
    =====
    for line in hand:
    =====
    for line in 'mbox-short.txt' #distractor
    =====
        line = line.rstrip()
    =====
        x = re.findall('^X\S*: ([0-9.]+)', line)
    =====
        if len(x) > 0:
    =====
        if len(hand) > 0: #distractor
    =====
            print(x)