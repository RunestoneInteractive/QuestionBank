.. mchoice:: mc8k
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Strings
   :subchapter: TraversalandtheforLoopByItem
   :topics: Strings/TraversalandtheforLoopByItem
   :from_source: None
   :answer_a: 4
   :answer_b: 5
   :answer_c: 6
   :answer_d: Error, the for statement cannot use slice.
   :correct: b
   :feedback_a: Slice returns a sequence that can be iterated over.
   :feedback_b: Yes, The blank is part of the sequence returned by slice
   :feedback_c: Check the result of s[3:8].  It does not include the item at index 8.
   :feedback_d: Slice returns a sequence.


   How many times is the word HELLO printed by the following statements?

   .. code-block:: python

      s = "python rocks"
      for ch in s[3:8]:
          print("HELLO")