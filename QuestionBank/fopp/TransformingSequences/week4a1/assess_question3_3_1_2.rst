.. mchoice:: assess_question3_3_1_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: week4a1
   :topics: TransformingSequences/week4a1
   :from_source: T
   :answer_a: yes
   :answer_b: no
   :feedback_a: Yes, b and z reference the same list and changes are made using both aliases.
   :feedback_b: Can you figure out what the value of b is only by looking at the lines that mention b?
   :correct: a
   :practice: T

   Could aliasing cause potential confusion in this problem?

   .. sourcecode:: python

    b = ['q', 'u', 'i']
    z = b
    b[1] = 'i'
    z.remove('i')
    print(z)