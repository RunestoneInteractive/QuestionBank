.. mchoice:: qListRem4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-4-arraylist-algorithms
   :topics: Unit7-ArrayList/topic-7-4-arraylist-algorithms
   :from_source: T
   :answer_a: [2, 3]
   :answer_b: [1, 2, 3]
   :answer_c: [1, 2]
   :answer_d: [1, 3]
   :correct: d
   :feedback_a: The <code>remove</code> will remove the item at the given index.
   :feedback_b: The item at index 1 will be removed and all the other values shifted left.
   :feedback_c: The 3 is at index 2.  The item at index 1 will be removed.
   :feedback_d: The item at index 1 is removed and the 3 is moved left.
   :pct_on_first: 0.7045149754
   :total_students_attempting: 2237
   :num_students_correct: 2213.0
   :mean_clicks_to_correct: 1.5282422052

   What will print when the following code executes?
   
   .. code-block:: java
   
      List<Integer> list1 = new ArrayList<Integer>();
      list1.add(new Integer(1));
      list1.add(new Integer(2));
      list1.add(new Integer(3));
      list1.remove(1);
      System.out.println(list1);