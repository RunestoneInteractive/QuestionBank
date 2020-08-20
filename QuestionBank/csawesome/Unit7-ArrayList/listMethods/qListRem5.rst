.. mchoice:: qListRem5
   :author: Brad Miller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: listMethods
   :topics: Unit7-ArrayList/listMethods
   :from_source: F
   :answer_a: [2, 3]
   :answer_b: [1, 2, 3]
   :answer_c: [1, 2]
   :answer_d: [1, 3]
   :correct: c
   :feedback_a: This would be true if it was <code>remove(0)</code>
   :feedback_b: The <code>remove</code> will remove a value from the list, so this can't be correct.
   :feedback_c: The 3 (at index 2) is removed
   :feedback_d: This would be true if it was <code>remove(1)</code>
   :pct_on_first: 0.8823529412
   :total_students_attempting: 17
   :num_students_correct: 17.0
   :mean_clicks_to_correct: 1.2352941176

   What will print when the following code executes?
   
   .. code-block:: java
   
      List<Integer> list1 = new ArrayList<Integer>();
      list1.add(new Integer(1));
      list1.add(new Integer(2));
      list1.add(new Integer(3));
      list1.remove(2);
      System.out.println(list1);