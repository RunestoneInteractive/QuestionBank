.. mchoice:: JP.1.1.a
   :author: John Pataracchia
   :difficulty: 2.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: Exercises
   :topics: Unit1-Getting-Started/Exercises
   :from_source: F
   :practice: T
   :answer_a: In line 1, print should be changed to println.
   :answer_b: In lines 2 and 3, println should be changed to print.
   :answer_c: The statement System.out.println() should be inserted between lines 2 and 3.
   :answer_d: In lines 1, 2, and 3, the text that appears in parentheses should be enclosed in quotation marks.
   :correct: d
   :feedback_a: The first and second sentences are printed on the same line so print() should be used on line 1.
   :feedback_b: The second and third lines are printed on different lines so println() should be used.
   :feedback_c: This would not resolve the error.
   :feedback_d: Yes! String literals must always be enclosed in quotes ("...").
   :pct_on_first: 0.5714285714
   :total_students_attempting: 42
   :num_students_correct: 35.0
   :mean_clicks_to_correct: 1.7714285714

       Consider the following code segment:
          System.out.print(I do not fear computers. );   // Line 1
   
          System.out.println(I fear the lack of them.);  // Line 2
   
          System.out.println(--Isaac Asimov);            // Line 3
   
   
       The code segment is intended to produce the following output but may not work as intended.
   
       I do not fear computers. I fear the lack of them.
   
       --Isaac Asimov
   ch change, if any, can be made so that the code segment produces the intended output?