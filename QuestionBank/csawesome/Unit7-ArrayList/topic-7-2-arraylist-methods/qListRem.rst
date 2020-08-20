.. mchoice:: qListRem
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-2-arraylist-methods
   :topics: Unit7-ArrayList/topic-7-2-arraylist-methods
   :from_source: T
   :answer_a: [2, 3]
   :answer_b: [1, 2, 3]
   :answer_c: [1, 2]
   :answer_d: [1, 3]
   :correct: c
   :feedback_a: This would be true if it was <code>remove(0)</code>
   :feedback_b: The <code>remove</code> will remove a value from the list, so this can't be correct.
   :feedback_c: The 3 (at index 2) is removed
   :feedback_d: This would be true if it was <code>remove(1)</code>
   :pct_on_first: 0.6996644295
   :total_students_attempting: 3576
   :num_students_correct: 3551.0
   :mean_clicks_to_correct: 1.4345254858

   What will print when the following code executes?
   
   .. code-block:: java
   
      List<Integer> list1 = new ArrayList<Integer>();
      list1.add(1);
      list1.add(2);
      list1.add(3);
      list1.remove(2);
      System.out.println(list1);