.. codelens:: WaitingIf2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPIntroDecisions
    :subchapter: noteWaitingIf
    :topics: CSPIntroDecisions/noteWaitingIf
    :from_source: T

    size = 0
    for i in [1, 2, 3, 4, 5]:
        size = size + 1
        print(size)
        if size == 5:
            print("Hello")