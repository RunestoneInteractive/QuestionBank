.. parsonsprob:: mixedupcode_question11_9
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
    use regular expressions to search for lines that start with 'Details: rev='
    followed by numbers and '.'. Then print the number of occurrences if it is greater
    than zero. The blocks have been mixed up, and include two extra blocks that are not correct.
    -----
    import re
    =====
    hand = open('mbox-short.txt')
    =====
    for line in hand:
    =====
        line = line.rstrip()
    =====
        x = re.findall('^Details:.*rev=([0-9.]+)', line)
    =====
        x = re.findall('^X\S*: ([0-9.]+)', line) #distractor
    =====
        if len(x) > 0:
    =====
        if len(x) < 0: #distractor
    =====
            print(x)