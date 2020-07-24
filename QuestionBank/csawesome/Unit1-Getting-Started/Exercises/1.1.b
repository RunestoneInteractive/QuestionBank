.. mchoice:: 1.1.b
   :author: Beryl Hoffman
   :difficulty: 3
   :basecourse: csawesome
   :topic: Unit1-Getting-Started/Exercises
   :from_source: F
   :practice: T
   :answer_a: In line 1, print should be changed to println.
   :answer_b: In lines 2 and 3, println should be changed to print.
   :answer_c: The statement System.out.println() should be inserted between lines 2 and 3.
   :answer_d: In lines 1, 2, and 3, the text that appears in parentheses should also be enclosed in quotation marks.
   :correct: d
   :feedback_a: There is something missing in these print statements!
   :feedback_b: There is something missing in these print statements!
   :feedback_c: There is something missing in these print statements!
   :feedback_d: Correct! Don't forget the "quotation marks"!

   Consider the following code segment:

   .. code-block:: java

              System.out.print(I do not fear computers. );   // Line 1
              System.out.println(I fear the lack of them.);  // Line 2
              System.out.println(--Isaac Asimov);            // Line 3

   The code segment is intended to produce the following output but may not work as intended.

   I do not fear computers. I fear the lack of them.

   --Isaac Asimov

   Which change, if any, can be made so that the code segment produces the intended output?