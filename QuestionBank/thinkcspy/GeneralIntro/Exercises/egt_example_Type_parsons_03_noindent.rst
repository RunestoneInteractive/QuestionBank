.. parsonsprob:: egt_example_Type_parsons_03_noindent
    :author: Eric Taucher (Instructor)
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: GeneralIntro
    :subchapter: Exercises
    :topics: GeneralIntro/Exercises
    :from_source: F
    :noindent: 
    :pct_on_first: 0.0
    :total_students_attempting: 8
    :num_students_correct: 7.0
    :mean_clicks_to_correct: 9.7142857143

    Solve my really cool parsons problem...if you can.
    -----
    def findmax(alist):
    =====
    if len(alist) == 0:
        return None
    =====
    curmax = alist[0]
    for item in alist:
    =====
        if item &gt; curmax:
    =====
            curmax = item
    =====
    return curmax