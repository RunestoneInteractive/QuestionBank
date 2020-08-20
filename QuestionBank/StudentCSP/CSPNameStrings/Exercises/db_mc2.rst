.. mchoice:: db_mc2
   :author: Barbara  Ericson
   :difficulty: 2.0
   :basecourse: StudentCSP
   :chapter: CSPNameStrings
   :subchapter: Exercises
   :topics: CSPNameStrings/Exercises
   :from_source: F
   :correct: d
   :answer_a: None
   :answer_b: 1
   :answer_c: 4
   :answer_d: 5
   :feedback_a: Each insert will insert data in the table.
   :feedback_b: This would be true if we only had one insert, but there are many.
   :feedback_c: This would be true if there was a primary key and it was insert or ignore.
   :feedback_d: It will do every insert, even if there is duplicate data since we didn't set up a primary key and didn't do insert or ignore.
   :pct_on_first: 0.5114503817
   :total_students_attempting: 131
   :num_students_correct: 131.0
   :mean_clicks_to_correct: 1.8091603053

   How many users will be in the Users table after this SQL executes?
   
    .. code-block:: python
   
       CREATE TABLE "Users" ("name" TEXT, "email" TEXT);
       INSERT INTO Users (name, email) VALUES ('Chuck', 'csev@umich.edu');
       INSERT INTO Users (name, email) VALUES ('Colleen', 'cvl@umich.edu');
       INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu');
       INSERT INTO Users (name, email) VALUES ('Sally', 'a1@umich.edu');
       INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu');
   ERT INTO Users (name, email) VALUES ('Kristen', 'kf@umich.edu');