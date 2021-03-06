.. mchoice:: mc7b
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: MoreAboutIteration
   :subchapter: SimpleTables
   :topics: MoreAboutIteration/SimpleTables
   :from_source: None
   :answer_a: Output a
   :answer_b: Output b
   :answer_c: Output c
   :answer_d: Output d
   :correct: a
   :feedback_a: i will start with a value of 0 and then j will iterate from 0 to 1.  Next, i will be 1 and j will iterate from 0 to 1.  Finally, i will be 2 and j will iterate from 0 to 1.
   :feedback_b: The inner for-loop controls the second digit (j).  The inner for-loop must complete before the outer for-loop advances.
   :feedback_c: The inner for-loop controls the second digit (j).  Notice that the inner for-loop is over the list [0, 1].
   :feedback_d: The outer for-loop runs 3 times (0, 1, 2) and the inner for-loop runs twice for each time the outer for-loop runs, so this code prints exactly 6 lines.

   What will the following nested for-loop print?  (Note, if you are having trouble with this question, review CodeLens 1).

   .. code-block:: python

      for i in range(3):
          for j in range(2):
              print(i, j)

   ::

      a.

      0 0
      0 1
      1 0
      1 1
      2 0
      2 1

      b.

      0   0
      1   0
      2   0
      0   1
      1   1
      2   1

      c.

      0   0
      0   1
      0   2
      1   0
      1   1
      1   2

      d.

      0   1
      0   1
      0   1