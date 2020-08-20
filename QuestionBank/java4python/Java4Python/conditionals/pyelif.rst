.. activecode:: pyelif
    :author: bmiller
    :difficulty: 3.0
    :basecourse: java4python
    :chapter: Java4Python
    :subchapter: conditionals
    :topics: Java4Python/conditionals
    :from_source: T
    :language: python

    grade = int(input('enter a grade'))
    if grade < 60:
        print('F')
    elif grade < 70:
        print('D')
    elif grade < 80:
        print('C')
    elif grade < 90:
        print('B')
    else:
        print('A')