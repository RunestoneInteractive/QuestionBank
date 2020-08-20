.. mchoice:: mcpydictperf
  :author: bmiller
  :difficulty: 3.0
  :basecourse: pythonds
  :chapter: AlgorithmAnalysis
  :subchapter: Dictionaries
  :topics: AlgorithmAnalysis/Dictionaries
  :from_source: T
  :answer_a: 'x' in mydict
  :answer_b: del mydict['x']
  :answer_c: mydict['x'] == 10
  :answer_d: mydict['x'] = mydict['x'] + 1
  :answer_e: all of the above are O(1)
  :correct: e
  :feedback_a: in is a constant operation for a dictionary because you do not have to iterate but there is a better answer.
  :feedback_b: deleting an element from a dictionary is a constant operation but there is a better answer.
  :feedback_c: Assignment to a dictionary key is constant but there is a better answer.
  :feedback_d: Re-assignment to a dictionary key is constant but there is a better answer.
  :feedback_e: The only dictionary operations that are not O(1) are those that require iteration.
  :pct_on_first: 0.6392844104
  :total_students_attempting: 2739
  :num_students_correct: 2717.0
  :mean_clicks_to_correct: 1.8075082812

  Which of the dictionary operations shown below is O(1)?