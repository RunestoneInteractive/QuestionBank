.. mchoice:: files_assessment_irma4
   :author: Irma Ravkic
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: Files
   :subchapter: Exercises
   :topics: Files/Exercises
   :from_source: F
   :answer_a: filevar.append(somestring)
   :answer_b: filevar.write("somestring")
   :answer_c: filevar.write(somestring)
   :answer_d: somestring.write()
   :feedback_a: append() is not used for files, but lists
   :feedback_b: this will write "somestring" to the file, and not "my Sentence" as we wanted.
   :feedback_c: correct.
   :feedback_d: string type variable doesn't have a function write().
   :correct: c
   :practice: T

   Which of the commands below is used to add a string ``somestring = "my Sentence"`` to the end of the file referenced by ``filevar`` variable.