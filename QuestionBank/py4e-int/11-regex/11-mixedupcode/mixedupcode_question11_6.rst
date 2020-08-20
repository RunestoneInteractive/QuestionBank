.. parsonsprob:: mixedupcode_question11_6
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

    The following code should create a new string "y" from the price included
    in the string "x". The blocks have been mixed up, and include two extra
    blocks that are not correct.
    -----
    import re
    =====
    x = 'We just received $10.00 for cookies.'
    =====
    y = re.findall('\$[0-9.]+',x)
    =====
    y = re.find('\$[0-9]+',x) #distractor
    =====
    y = re.findall('$[0-9]+',x) #distractor