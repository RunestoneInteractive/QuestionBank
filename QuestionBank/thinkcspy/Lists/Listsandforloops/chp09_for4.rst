.. activecode:: chp09_for4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Lists
    :subchapter: Listsandforloops
    :topics: Lists/Listsandforloops
    :from_source: T

    numbers = [1, 2, 3, 4, 5]
    print(numbers)

    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2

    print(numbers)