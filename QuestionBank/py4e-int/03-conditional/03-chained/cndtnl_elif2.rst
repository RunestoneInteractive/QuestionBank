.. codelens:: cndtnl_elif2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 03-conditional
    :subchapter: 03-chained
    :topics: 03-conditional/03-chained
    :from_source: T
    :showoutput:
    :question: After the line with the red arrow is executed, which line will be next?
    :breakline: 2
    :feedback: Remember that in an if/else statement only one block is executed.
    :correct: line

    choice = 'b'
    if choice == 'a':
        print('Bad guess')
    elif choice == 'b':
        print('Good guess')
    elif choice == 'c':
        print('Close, but not correct')