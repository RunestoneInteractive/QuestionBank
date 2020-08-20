.. mchoice:: mcpyperform
   :author: bmiller
   :difficulty: 3.0
   :basecourse: pythonds3
   :chapter: AlgorithmAnalysis
   :subchapter: Dictionaries
   :topics: AlgorithmAnalysis/Dictionaries
   :from_source: T
   :answer_a: a_list.pop(0)
   :answer_b: a_list.pop()
   :answer_c: a_list.append()
   :answer_d: a_list[10]
   :answer_e: all of the above are O(1)
   :correct: a
   :feedback_a: When you remove the first element of a list, all the other elements of the list must be shifted forward.
   :feedback_b: Removing an element from the end of the list is a constant operation.
   :feedback_c: Appending to the end of the list is a constant operation
   :feedback_d: Indexing a list is a constant operation
   :feedback_e: There is one operation that requires all other list elements to be moved.
   :pct_on_first: 1.0
   :total_students_attempting: 15
   :num_students_correct: 15
   :mean_clicks_to_correct: 1.0

   Which of the list operations shown below is not O(1)?