.. mchoice:: qalm_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: listMedMC
   :topics: Unit7-ArrayList/listMedMC
   :from_source: T
   :practice: T
   :answer_a: [1, 2, 3, 4, 5]
   :answer_b: [1, 2, 4, 5, 6]
   :answer_c: [1, 2, 5, 4, 6]
   :answer_d: [1, 5, 2, 4, 6]
   :correct: c
   :feedback_a: The set replaces the 3 at index 2 with the 4 so this can't be right.
   :feedback_b: The add with an index of 2 and a value of 5 adds the 5 at index 2 not 3.  Remember that the first index is 0.
   :feedback_c: The add method that takes just an object as a parameter adds that object to the end of the list.  The set replaces the value at that index with the new value.  The add with parameters of an index and an object puts the passed object at that index and moves any existing values by one index to the right (increments the index).
   :feedback_d: The add with an index of 2 and a value of 5 adds the 5 at index 2 not 1.  Remember that the first index is 0.
   :pct_on_first: 0.6510103768
   :total_students_attempting: 1831
   :num_students_correct: 1794.0
   :mean_clicks_to_correct: 1.5178372352

   What is printed as a result of executing the following code segment?
   
   .. code-block:: java
   
      List<Integer> list1 = new ArrayList<Integer>();
      list1.add(new Integer(1));
      list1.add(new Integer(2));
      list1.add(new Integer(3));
      list1.set(2, new Integer(4));
      list1.add(2, new Integer(5));
      list1.add(new Integer(6));
      System.out.println(list1);