.. activecode:: pyelif
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: Control_Structures
    :subchapter: conditionals
    :topics: Control_Structures/conditionals
    :from_source: T
    :language: python

    # demonstrates if,elif, and else statements in python
    def main():
        grade = 85

        if (grade < 60):
            print('F')
        elif (grade < 70):
            print('D')
        elif grade < 80:
            print('C')
        elif grade < 90:
            print('B')
        else:
            print('A')

    main()