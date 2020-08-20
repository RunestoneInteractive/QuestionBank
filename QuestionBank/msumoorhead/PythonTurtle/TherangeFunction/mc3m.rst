.. mchoice:: mc3m
  :author: jenkins
  :difficulty: 3.0
  :basecourse: msumoorhead
  :chapter: PythonTurtle
  :subchapter: TherangeFunction
  :topics: PythonTurtle/TherangeFunction
  :from_source: None
  :answer_a: It will generate a sequence starting at 0, with every number included up to but not including the argument it was passed.
  :answer_b: It will generate a sequence starting at 1, with every number up to but not including the argument it was passed.
  :answer_c: It will generate a sequence starting at 1, with every number including the argument it was passed.
  :answer_d: It will cause an error: range always takes exactly 3 arguments.
  :correct: a
  :feedback_a: Yes, if you only give one number to range it starts with 0 and ends before the number specified incrementing by 1.
  :feedback_b: Range with one parameter starts at 0.
  :feedback_c: Range with one parameter starts at 0, and never includes its ending element (which is the argument it was passed).
  :feedback_d: If range is passed only one argument, it interprets that argument as the end of the list (not inclusive).

  What happens if you give range only one argument?  For example: range(4)