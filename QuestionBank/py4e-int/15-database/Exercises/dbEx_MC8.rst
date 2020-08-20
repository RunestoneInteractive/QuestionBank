.. mchoice:: dbEx_MC8
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 15-database
    :subchapter: Exercises
    :topics: 15-database/Exercises
    :from_source: T
    :practice: T
    :answer_a: True
    :answer_b: False
    :correct: a
    :feedback_a: * indicates that you want the database to return all of the columns for each row that matches the WHERE clause.
    :feedback_b: Try again!

    True or False? The following line will select all columns for the name "Bernard" from the table "Cats".

    ::

      SELECT * FROM Cats WHERE name = 'Bernard'