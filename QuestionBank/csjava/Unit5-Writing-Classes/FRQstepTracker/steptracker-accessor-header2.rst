.. mchoice:: steptracker-accessor-header2
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit5-Writing-Classes/FRQstepTracker
   :from_source: T
   :practice: T
   :answer_a: public void averageSteps()
   :answer_b: public int averageSteps()
   :answer_c: public double averageSteps()
   :answer_d: public void averageSteps(int numSteps)
   :answer_e: public int averageSteps(int numSteps)
   :correct: c
   :feedback_a: Accessor methods need a return type since they return the value of an instance variable or a value calculated from instance variables.
   :feedback_b: When you compute an average using division, you usually end up with a double value, not int.
   :feedback_c: Correct, accessor methods are public, have a return type, and no parameter. In this case, returning an average requires a double return type.
   :feedback_d: Accessor methods need a return type since they return the value of an instance variable or a value calculated from instance variables, and  they do not usually have a parameter.
   :feedback_e: Accessor methods do not usually take parameters.

   Which of the following is a good method header for the accessor method averageSteps() which returns the average number of steps per day?