.. mchoice:: mc6h
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Selection
   :subchapter: PrecedenceofOperators
   :topics: Selection/PrecedenceofOperators
   :from_source: None
   :answer_a: ((5*3) &gt; 10) and ((4+6) == 11)
   :answer_b: (5*(3 &gt; 10)) and (4 + (6 == 11))
   :answer_c: ((((5*3) &gt; 10) and 4)+6) == 11
   :answer_d: ((5*3) &gt; (10 and (4+6))) == 11
   :correct: a
   :feedback_a: Yes, * and + have higher precedence, followed by &gt; and ==, and then the keyword &quot;and&quot;
   :feedback_b: Arithmetic operators (*, +) have higher precedence than comparison operators (&gt;, ==)
   :feedback_c: This grouping assumes Python simply evaluates from left to right, which is incorrect.  It follows the precedence listed in the table in this section.
   :feedback_d: This grouping assumes that &quot;and&quot; has a higher precedence than ==, which is not true.

   Which of the following properly expresses the precedence of operators (using parentheses) in the following expression: 5*3 > 10 and 4+6==11