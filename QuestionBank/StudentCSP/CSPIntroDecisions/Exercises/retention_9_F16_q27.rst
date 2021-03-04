.. mchoice:: retention_9_F16_q27
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPIntroDecisions
   :subchapter: Exercises
   :topics: CSPIntroDecisions/Exercises
   :from_source: F
   :answer_a: C?T
   :answer_b: EaV
   :answer_c: E?V
   :answer_d: There is an error
   :answer_e: None
   :feedback_a: Incorrect!
   :feedback_b: Incorrect!
   :feedback_c: Correct!
   :feedback_d: Incorrect!
   :feedback_e: Incorrect!
   :correct: c
   :practice: T

   What is the output of the following code? If there is an error, say so.

   .. sourcecode:: python

      def crypt(s, n=2, L='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
         rv = ''
         for letter in s:
            try:
               idx = L.index(letter)
               rotated_idx = (idx+n)%len(L)
               rv += L[rotated_idx]
            except:
               rv += '?'
         return rv

      print (crypt('CaT'))