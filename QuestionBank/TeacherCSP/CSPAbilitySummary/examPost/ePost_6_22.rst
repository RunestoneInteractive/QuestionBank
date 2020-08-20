.. mchoice:: ePost_6_22
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPAbilitySummary
   :subchapter: examPost
   :topics: CSPAbilitySummary/examPost
   :from_source: T
   :answer_a: The printed result will be odd with a decimal point.
   :answer_b: The printed result will be even with a decimal point.
   :answer_c: The printed result will be odd without a decimal point.
   :answer_d: The printed result will be even without a decimal point.
   :correct: d
   :feedback_a: This would true if there was an odd numer of items in aList and at least one of the numbers had a decimal point.
   :feedback_b: This would true if at least one of the numbers had a decimal point.
   :feedback_c: This would true if there was an odd numer of items in aList.
   :feedback_d: Since you are adding up an even number of odd numbers the answer will be even. Since all numbers are integers (don't have a decimal point) the answer won't have a decimal point either.

   Given the following code segment, which of the below statements is the most true?

   ::

      sum = 0
      aList = [1,3,7,19,21,131]
      for number in aList:
          sum = sum + number
      print (sum)