.. mchoice:: mc8h
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Strings
   :subchapter: TheSliceOperator
   :topics: Strings/TheSliceOperator
   :from_source: None
   :answer_a: rockrockrock
   :answer_b: rock rock rock
   :answer_c: rocksrocksrocks
   :answer_d: Error, you cannot use repetition with slicing.
   :correct: a
   :feedback_a: Yes, rock starts at 7 and goes through 10.  Repeat it 3 times.
   :feedback_b: Repetition does not add a space.
   :feedback_c: Slicing will not include the character at index 11.  Just up to it (10 in this case).
   :feedback_d: The slice will happen first, then the repetition.  So it is ok.


   What is printed by the following statements?

   .. code-block:: python

      s = "python rocks"
      print(s[7:11] * 3)