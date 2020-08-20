.. parsonsprob:: mixedupcode_question11_8
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

    The following code should read all the lines in a file, remove whitespace, and
    use regular expressions to find and print out anything lines that start with “From:”,
    followed by one or more characters, followed by an at-sign. The blocks have been
    mixed up, and include two extra blocks that are not correct.
    -----
    import re
    =====
    hand = open('mbox-short.txt')
    =====
    for line in hand:
    =====
        line = line.rstrip()
    =====
        if re.search('^From:.+@', line):
    =====
        if re.search('^F..m:', line): #distractor
    =====
            print(line)
    =====
            print(hand) #distractor