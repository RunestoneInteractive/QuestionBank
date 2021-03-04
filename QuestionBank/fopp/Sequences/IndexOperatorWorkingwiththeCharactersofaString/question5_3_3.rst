.. mchoice:: question5_3_3
   :author: bmiller
   :difficulty: 2.6222318715
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: IndexOperatorWorkingwiththeCharactersofaString
   :topics: Sequences/IndexOperatorWorkingwiththeCharactersofaString
   :from_source: T
   :answer_a: [ ]
   :answer_b: 3.14
   :answer_c: False
   :answer_d: "dog"
   :correct: b
   :feedback_a: The empty list is at index 4.
   :feedback_b: Yes, 3.14 is at index 5 since we start counting at 0 and sublists count as one item.
   :feedback_c: False is at index 6.
   :feedback_d: Look again, the element at index 3 is a list. This list only counts as one element.
   :practice: T
   :pct_on_first: 0.5944420321
   :total_students_attempting: 2303
   :num_students_correct: 2295.0
   :mean_clicks_to_correct: 1.6087145969

   What is printed by the following statements?
   
   .. code-block:: python
   
     alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
     print(alist[5])