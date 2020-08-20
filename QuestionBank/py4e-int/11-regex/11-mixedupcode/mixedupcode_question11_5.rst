.. parsonsprob:: mixedupcode_question11_5
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

    The following code should use create a regular expression pattern that can match
    the following phrases: <br>
    "Sincerely, Molly" <br>"Sincerely, &nbsp; Molly" <br>"Sincerely,<br>Molly" <br> and
    test it on the sequence. If they are the same, it should print "Match!", if not it
    should print "Not a match!". The blocks have been mixed up, and include two extra
    blocks that are not correct. Watch out for the extra blocks and indentation!
    -----
    import re
    =====
    pattern = r"Sincerely,\Molly"
    =====
    pattern = r"Sincerely, *Molly" #distractor
    =====
    pattern = r"Sincerely, .* Molly" #distractor
    =====
    sequence = "Sincerely,       Molly"
    =====
    if re.match(pattern, sequence):
    =====
        print("Match!")
    =====
    else:
    =====
        print("Not a match!")