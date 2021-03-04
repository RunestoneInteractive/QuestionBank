.. mchoice:: assess_question3_3_1_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: week4a1
   :topics: TransformingSequences/week4a1
   :from_source: T
   :answer_a: yes
   :answer_b: no
   :feedback_a: Since a string is immutable, aliasing won't be as confusing. Beware of using something like item = item + new_item with mutable objects though because it creates a new object. However, when we use += then that doesn't happen.
   :feedback_b: Since a string is immutable, aliasing won't be as confusing. Beware of using something like item = item + new_item with mutable objects though because it creates a new object. However, when we use += then that doesn't happen.
   :correct: b
   :practice: T

   Could aliasing cause potential confusion in this problem?

   .. sourcecode:: python

    sent = "Holidays can be a fun time when you have good company!"
    phrase = sent
    phrase = phrase + " Holidays can also be fun on your own!"