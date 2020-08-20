.. parsonsprob:: listMixed_months
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-MixedupCode
    :topics: 08-lists/08-MixedupCode
    :from_source: T
    :numbered: left
    :practice: T
    :adaptive:

    The following program segment should first replace the last item of the list <i>months</i> with
    "November" then append "December" to the end of the list. But, the blocks have been mixed up and
    include extra blocks that aren't needed in the solution.
    -----
    months = ["January", "March", "June", "August", "October"]
    new_month = "November"
    =====
    months[4] = new_month
    =====
    months.append("December")
    =====
    months[5] = new_month #distractor
    =====
    months[-1] = "December" #distractor