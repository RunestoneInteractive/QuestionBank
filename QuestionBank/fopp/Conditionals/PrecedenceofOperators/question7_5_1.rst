.. mchoice:: question7_5_1
   :author: bmiller
   :difficulty: 1.8427095293
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: PrecedenceofOperators
   :topics: Conditionals/PrecedenceofOperators
   :from_source: T
   :answer_a: ((5*3) &gt; 10) and ((4+6) == 11)
   :answer_b: (5*(3 &gt; 10)) and (4 + (6 == 11))
   :answer_c: ((((5*3) &gt; 10) and 4)+6) == 11
   :answer_d: ((5*3) &gt; (10 and (4+6))) == 11
   :correct: a
   :feedback_a: Yes, * and + have higher precedence, followed by &gt; and ==, and then the keyword &quot;and&quot;
   :feedback_b: Arithmetic operators (*, +) have higher precedence than comparison operators (&gt;, ==)
   :feedback_c: This grouping assumes Python simply evaluates from left to right, which is incorrect.  It follows the precedence listed in the table in this section.
   :feedback_d: This grouping assumes that &quot;and&quot; has a higher precedence than ==, which is not true.
   :practice: T
   :pct_on_first: 0.7893226177
   :total_students_attempting: 1742
   :num_students_correct: 1732.0
   :mean_clicks_to_correct: 1.4595842956

   Which of the following properly expresses the  precedence of operators (using parentheses) in the following expression: 5*3 > 10 and 4+6==11