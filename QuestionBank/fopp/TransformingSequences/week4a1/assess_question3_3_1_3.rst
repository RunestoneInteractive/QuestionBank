.. mchoice:: assess_question3_3_1_3
   :author: Brad Miller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: week4a1
   :topics: TransformingSequences/week4a1
   :from_source: F
   :answer_a: yes
   :answer_b: no
   :feedback_a: Though both lists have changed, it is not as likely to cause confusion.
   :feedback_b: These operations on the lists are not likely to cause confusion.
   :correct: b
   :practice: T

   Could aliasing cause potential confusion in this problem?

   .. sourcecode:: python

    b = ['q', 'u', 'i']
    z = b
    b[1] = 'i'
    for elem in b:
        print(elem)
    for item in z:
        print(item)