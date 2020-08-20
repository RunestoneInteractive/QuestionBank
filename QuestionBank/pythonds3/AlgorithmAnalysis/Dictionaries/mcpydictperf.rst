.. mchoice:: mcpydictperf
  :author: bmiller
  :difficulty: 3.0
  :basecourse: pythonds3
  :chapter: AlgorithmAnalysis
  :subchapter: Dictionaries
  :topics: AlgorithmAnalysis/Dictionaries
  :from_source: T
  :answer_a: "x" in a_dict
  :answer_b: del a_dict["x"]
  :answer_c: a_dict["x"] == 10
  :answer_d: a_dict["x"] = a_dict["x"] + 1
  :answer_e: all of the above are O(1)
  :correct: e
  :feedback_a: in is a constant operation for a dictionary because you do not have to iterate but there is a better answer.
  :feedback_b: deleting an element from a dictionary is a constant operation but there is a better answer.
  :feedback_c: Assignment to a dictionary key is constant but there is a better answer.
  :feedback_d: Re-assignment to a dictionary key is constant but there is a better answer.
  :feedback_e: The only dictionary operations that are not O(1) are those that require iteration.
  :pct_on_first: 0.625
  :total_students_attempting: 16
  :num_students_correct: 16
  :mean_clicks_to_correct: 1.875

  Which of the dictionary operations shown below is O(1)?