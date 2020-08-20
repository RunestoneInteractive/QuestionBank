.. activecode:: ch7ex1a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatNumbers
    :subchapter: ch7_exercises
    :topics: CSPRepeatNumbers/ch7_exercises
    :from_source: T
    :nocodelens:

    sum = 0  # Start out with nothing
    thingsToAdd = [1,2,3,4,5]
    for number in thingsToAdd:
        sum = sum + number
    print(sum)