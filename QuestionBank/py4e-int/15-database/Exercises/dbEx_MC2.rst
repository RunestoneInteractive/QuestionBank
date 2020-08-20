.. mchoice:: dbEx_MC2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 15-database
    :subchapter: Exercises
    :topics: 15-database/Exercises
    :from_source: T
    :practice: T
    :answer_a: It will remove the Tuple "Cats".
    :answer_b: It will move "Cats" to the end of the database.
    :answer_c: It will remove the Attribute "Cats".
    :answer_d: It will remove the Relation "Cats".
    :correct: d
    :feedback_a: "Cats" is not a tuple (row).
    :feedback_b: That's not quite what drop means in SQL.
    :feedback_c: "Cats" is not an attribute (column).
    :feedback_d: "Cats" is a relation (table), so this line will remove it from the database.

    Looking at the code below, what would this line do to the table ``Cats``?

    ::

      cur.execute('DROP TABLE IF EXISTS Cats ')