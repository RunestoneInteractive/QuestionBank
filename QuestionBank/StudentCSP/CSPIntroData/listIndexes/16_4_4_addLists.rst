.. mchoice:: 16_4_4_addLists
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPIntroData
   :subchapter: listIndexes
   :topics: CSPIntroData/listIndexes
   :from_source: T
   :practice: T
   :answer_a: [3, 2, 1]
   :answer_b: [2, 0, 2]
   :answer_c: [2, 2, 2]
   :answer_d: [2, 2, 1]
   :correct: c
   :feedback_a: That is the original contents of <code>values</code>, but the contents are changed.
   :feedback_b: When you set <code>values[0]</code> to <code>values[1]</code> it makes a copy of the value and doesn't zero it out.
   :feedback_c: The value at index 0 is set to a copy of the value at index 1 and the value at index 2 is incremented.
   :feedback_d: Notice that we do change the value at index 2.  It is incremented by 1.
   :pct_on_first: 0.597955707
   :total_students_attempting: 587
   :num_students_correct: 579.0
   :mean_clicks_to_correct: 1.6580310881

   What would the following code print?
   
   ::
   
      values = [3, 2, 1]
      values[0] = values[1]
      values[2] = values[2] + 1
      print(values)