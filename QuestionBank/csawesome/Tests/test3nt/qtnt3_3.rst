.. mchoice:: qtnt3_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test3nt
   :topics: Tests/test3nt
   :from_source: T
   :answer_a: [7, 1, 4, 8, 3]
   :answer_b: [7, 8, 1, 2, 4, 3]
   :answer_c: [7, 3, 1, 4, 3]
   :answer_d: [8, 1, 2, 4, 3]
   :answer_e: [7, 8, 1, 4, 3]
   :correct: e
   :feedback_a: Remember that in ArrayLists, indexing starts at 0, not at 1. If the add method has two parameters, then the value is added at a specific index, not at the end of the list.
   :feedback_b: The set method replaces a value at the specific index. The original value is erased.
   :feedback_c: Remember that there are two add methods for ArrayLists. If the add method has two parameters, then a value is added at a specific index, not at the end of the list.
   :feedback_d: Remember that in ArrayLists, indexing starts at 0, not at 1.
   :feedback_e: 4 is added to the end of the ArrayList, then 8 is added at index one between 7 and 3. The 3 in index two is removed, then the 2 in the second index is replaced with 1. Finally, 3 is added to the end of the ArrayList, which contains [7, 8, 1, 4, 3].
   :pct_on_first: 0.5819672131
   :total_students_attempting: 122
   :num_students_correct: 118.0
   :mean_clicks_to_correct: 1.8813559322

   Consider the following code. Assume that ``list`` is an ArrayList of integers that contains ``[7, 3, 2]``. What will the contents of ``list`` be after the following code is executed?
   
   .. code-block:: java
   
      list.add(4);
      list.add(1, 8);
      list.remove(2);
      list.set(2, 1);
      list.add(3);