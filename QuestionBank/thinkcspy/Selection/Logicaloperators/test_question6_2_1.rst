.. mchoice:: test_question6_2_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Selection
   :subchapter: Logicaloperators
   :topics: Selection/Logicaloperators
   :from_source: T
   :practice: T
   :answer_a: x &gt; 0 and &lt; 5
   :answer_b: x &gt; 0 or x &lt; 5
   :answer_c: x &gt; 0 and x &lt; 5
   :correct: c
   :feedback_a: Each comparison must be between exactly two values.  In this case the right-hand expression &lt; 5 lacks a value on its left.
   :feedback_b: Although this is legal Python syntax, the expression is incorrect.  It will evaluate to true for all numbers that are either greater than 0 or less than 5.  Because all numbers are either greater than 0 or less than 5, this expression will always be True.
   :feedback_c: Yes, with an and keyword both expressions must be true so the number must be greater than 0 an less than 5 for this expression to be true. Although most other programming languages do not allow this mathematical syntax, in Python, you could also write 0 &lt; x &lt; 5.
   :pct_on_first: 0.6256611166
   :total_students_attempting: 15315
   :num_students_correct: 15246.0
   :mean_clicks_to_correct: 1.4982946347

   What is a correct Python expression for checking to see if a number stored in a variable x is between 0 and 5?