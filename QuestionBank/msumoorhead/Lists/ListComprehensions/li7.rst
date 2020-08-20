.. activecode:: li7
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Lists
    :subchapter: ListComprehensions
    :topics: Lists/ListComprehensions
    :from_source: None

    numbers = [1,2,3,5,8,13]

    squares = [val**2 for val in numbers]
    print(squares)