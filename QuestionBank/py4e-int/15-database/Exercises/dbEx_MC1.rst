.. mchoice:: dbEx_MC1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 15-database
    :subchapter: Exercises
    :topics: 15-database/Exercises
    :from_source: T
    :practice: T
    :answer_a: Add a Tuple to Cats with the name "Petunia" and breed "American Shorthair".
    :answer_b: Add an Attribute to Cats with the name "Petunia" and breed "American Shorthair".
    :answer_c: Create the Relation Cats.
    :answer_d: Add a database for the American Shorthair, Petunia.
    :correct: b
    :feedback_a: This line would add the tuple (row) for Petunia, American Shorthair, to the table Cats.
    :feedback_b: This line wouldn't add an attribute (column).
    :feedback_c: This line wouldn't create a new relation (table) for Petunia.
    :feedback_d: This line wouldn't create a new database for Petunia.

    Looking at the code below, what would this line do to the table ``Cats``?

    ::

      INSERT INTO Cats (name, breed) VALUES ('Petunia', 'American Shorthair')