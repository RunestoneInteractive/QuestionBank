.. parsonsprob:: mixedupcode_question11_7
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
    use regular expressions to find and print out anything that looks like an email
    address. The blocks have been mixed up, and include two extra blocks that are not correct.
    -----
    import re
    =====
    hand = open('mbox-short.txt')
    =====
    for line in hand:
    =====
        line = line.rstrip()
    =====
        x = re.findall('\S+@\S+', line)
    =====
        x = re.find('\S+@\S', line) #distractor
    =====
        x = re.findall('[A-Z]+@.*', line) #distractor
    =====
        if len(x) > 0:
    =====
            print(x)