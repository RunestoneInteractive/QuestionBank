.. activecode:: While2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroDecisions
    :subchapter: noteWhileExits
    :topics: CSPIntroDecisions/noteWhileExits
    :from_source: T

    while 1 == 1:
        print("This line gets executed (but only once!)")
        break      # loop exits here
        print("This line doesn't get executed")
        print("Neither does this")

    print("Outside of the loop")