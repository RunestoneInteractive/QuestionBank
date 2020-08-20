.. activecode:: str_q5_answer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: Exercises
    :topics: Strings/Exercises
    :from_source: T

    def numDigits(n):
        n_str = str(n)
        return len(n_str)


    print(numDigits(50))
    print(numDigits(20000))
    print(numDigits(1))