.. activecode:: itr-ex-countdowna
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 05-iterations
    :subchapter: 05-WriteCode
    :topics: 05-iterations/05-WriteCode
    :from_source: T

    def countdown():
        counter = 10
        while counter >= 0:
            print(counter)
            counter = counter - 1

    countdown()