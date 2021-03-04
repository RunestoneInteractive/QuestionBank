.. mchoice:: files_assessment_irma3
   :author: Irma Ravkic
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: Files
   :subchapter: Exercises
   :topics: Files/Exercises
   :from_source: F
   :answer_a: "myText".close()
   :answer_b: ref_file.close()
   :answer_c: close(ref_file)
   :answer_d: close("myText")
   :feedback_a: error in Python. String doesn't have function close().
   :feedback_b: correct.
   :feedback_c: close() must be called on a variable referencing the file.
   :feedback_d: close() must be called on a variable referencing the file.
   :correct: b
   :practice: T

   Which command below closes an already open file ``myText.txt`` with ``ref_file = open("myText.txt", "r")``??