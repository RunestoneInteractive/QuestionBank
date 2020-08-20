.. mchoice:: question7_3_1
   :author: bmiller
   :difficulty: 2.8914074855
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: Logicaloperators
   :topics: Conditionals/Logicaloperators
   :from_source: T
   :answer_a: x &gt; 0 and &lt; 5
   :answer_b: 0 &lt; x &lt; 5
   :answer_c: x &gt; 0 or x &lt; 5
   :answer_d: x &gt; 0 and x &lt; 5
   :correct: b,d
   :feedback_a: Each comparison must be between exactly two values.  In this case the right-hand expression &lt; 5 lacks a value on its left.
   :feedback_b: Although most other programming languages do not allow this syntax, in Python, this syntax is allowed.  Even though it is possible to use this format, you should not use it all the time.  Instead, make multiple comparisons by using and or or.
   :feedback_c: Although this is legal Python syntax, the expression is incorrect.  It will evaluate to true for all numbers that are either greater than 0 or less than 5.  Because all numbers are either greater than 0 or less than 5, this expression will always be True.
   :feedback_d: Yes, with an ``and`` keyword both expressions must be true so the number must be greater than 0 an less than 5 for this expression to be true.
   :practice: T
   :pct_on_first: 0.5271481286
   :total_students_attempting: 1897
   :num_students_correct: 1888.0
   :mean_clicks_to_correct: 1.7865466102

   What is the correct Python expression for checking to see if a number stored in a variable x is between 0 and 5.