.. activecode:: egt_example_Type_activecode_06_codelens
    :author: Eric Taucher (Instructor)
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: GeneralIntro
    :subchapter: Exercises
    :topics: GeneralIntro/Exercises
    :from_source: F

    def fibRec(n):
        if n < 2:
            return n
        else:
            return fibRec(n-1) + fibRec(n-2)
        
    n = int(input("N < 100"))
    result = fibRec(n)
    print("Fibonacci(",n,"):",result)