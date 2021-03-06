.. mchoice:: question14_7_3
   :author: bmiller
   :difficulty: 2.3818646232
   :basecourse: fopp
   :chapter: Iteration
   :subchapter: NestedIterationImageProcessing
   :topics: Iteration/NestedIterationImageProcessing
   :from_source: T
   :answer_a: Output a
   :answer_b: Output b
   :answer_c: Output c
   :answer_d: Output d
   :correct: a
   :feedback_a: i will start with a value of 0 and then j will iterate from 0 to 1. Next, i will be 1 and j will iterate from 0 to 1.  Finally, i will be 2 and j will iterate from 0 to 1.
   :feedback_b: The inner for-loop controls the second digit (j). The inner for-loop must complete before the outer for-loop advances.
   :feedback_c: The inner for-loop controls the second digit (j). Notice that the inner for-loop is over the list [0, 1].
   :feedback_d: The outer for-loop runs 3 times (0, 1, 2) and the inner for-loop runs twice for each time the outer for-loop runs, so this code prints exactly 6 lines.
   :pct_on_first: 0.6545338442
   :total_students_attempting: 1566
   :num_students_correct: 1555.0
   :mean_clicks_to_correct: 1.7536977492

   What will the following nested for-loop print? (Note, if you are having trouble with this question, review CodeLens 3).
   
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