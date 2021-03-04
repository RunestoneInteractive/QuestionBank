.. mchoice:: assess_question1_3_1_1_6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: PythonTurtle
   :subchapter: week1a3
   :topics: PythonTurtle/week1a3
   :from_source: T
   :answer_a: student.title()
   :answer_b: title.student()
   :answer_c: title.student
   :answer_d: student(title)
   :answer_e: student.title
   :correct: e
   :feedback_a: This accesses the attribute but then tries to invoke it as a method, which will fail if title is not a method.
   :feedback_b: student is the object, so it goes before the period; the attribute goes after.
   :feedback_c: student is the object, so it goes before the period; the attribute goes after.
   :feedback_d: This would be the syntax for a function named student being called on a variable named title.
   :feedback_e: Yes, this is the correct syntax to use.
   :practice: T

   For an instance of a class that is assigned to the variable ``student``, what is the proper way to refer to the ``title`` attribute/instance variable?