.. mchoice:: assess_question5_2_1_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: week4a1
   :topics: TransformingSequences/week4a1
   :from_source: T
   :answer_a: 1.
   :answer_b: 2.
   :answer_c: 3.
   :answer_d: 4.
   :answer_e: none of the above would be appropriate for the problem.
   :correct: d
   :feedback_a: How does this solution know that the element of lst is a string and that s should be updated?
   :feedback_b: What happens to s each time the for loop iterates?
   :feedback_c: Reread the prompt again, what do we want to accumulate?
   :feedback_d: Yes, this will solve the problem.
   :feedback_e: One of the patterns above is a correct way to solve the problem.
   :practice: T

   Given that we want to accumulate the total number of strings in the list, which of the following accumulator patterns would be appropriate?

   1.

   .. sourcecode:: python

    lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
    s = 0
    for n in lst:
        s = s + n

   2.

   .. sourcecode:: python

    lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
    for item in lst:
        s = 0
        if type(item) == type("string"):
            s = s + 1

   3.

   .. sourcecode:: python

    lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
    s = ""
    for n in lst:
        s = s + n

   4.

   .. sourcecode:: python

    lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
    s = 0
    for item in lst:
        if type(item) == type("string"):
            s = s + 1