.. parsonsprob:: mixedupcode_question11_3
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

    The following code should use regular expressions to print each item in the list
    "greetings", if it includes an "o". The blocks have been mixed up, and include
    two extra blocks that are not correct. Watch out for the extra blocks and indentation!
    -----
    import re
    =====
    greetings = ["Hello!", "hello.", "Good Morning!", "good morning!", "Good morning!", "hi"]
    =====
    for item in greetings:
    =====
        if re.search('o', item):
    =====
        if re('0', item): #distractor
    =====
        if re('^o', item): #distractor
    =====
            print(item)