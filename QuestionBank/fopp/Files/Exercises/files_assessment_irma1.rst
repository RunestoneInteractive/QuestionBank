.. mchoice:: files_assessment_irma1
   :author: Irma Ravkic
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: Files
   :subchapter: Exercises
   :topics: Files/Exercises
   :from_source: F
   :answer_a: infile = open(myText.txt, “r”)
   :answer_b: infile = open("myText.txt", “r”)
   :answer_c: infile = open("myText.txt", “w”)
   :feedback_a: Beware of variable name versus string value. Python will think myText.txt is a variable name here (which by the way is not a valid variable name). Check Note in 10.2
   :feedback_b: This is correct. We provide a string with file name + "r" which means read only.
   :feedback_c: Incorrect since "w" denotes writing, not readig.
   :correct: b
   :practice: T

   Which of the following commands is used to open a file called ``myText.txt`` in Read-Only mode?