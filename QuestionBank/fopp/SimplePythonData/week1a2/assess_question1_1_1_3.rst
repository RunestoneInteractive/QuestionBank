.. mchoice:: assess_question1_1_1_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: week1a2
   :topics: SimplePythonData/week1a2
   :from_source: T
   :multiple_answers:
   :answer_a: a = len("hello worldwelcome!")
   :answer_b: a = 11 + 8
   :answer_c: a = len(z) + len(y)
   :answer_d: a = len("hello world") + len("welcome!")
   :answer_e: none of the above are hardcoding.
   :feedback_a: Though we are using the len function here, we are hardcoding what len should return the length of. We are not referencing z or y.
   :feedback_b: This is hardcoding, we are writing in the value without referencing z or y.
   :feedback_c: This is not considered hard coding. We are using the function len to determine the length of what is stored in z and y, which is a correct way to approach this problem.
   :feedback_d: Though we are using the len function here, we are hardcoding what len should return the length of each time we call len. We are not referencing z or y.
   :feedback_e: At least one of these solutions is considered hardcoding. Take another look.
   :correct: a,b,d
   :practice: T

   The code below initializes two variables, ``z`` and ``y``. We want to assign the total number of characters in ``z`` and in ``y`` to the variable ``a``. Which of the following solutions, if any, would be considered hard coding?

   .. sourcecode:: python

    z = "hello world"
    y = "welcome!"