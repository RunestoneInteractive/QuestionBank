.. mchoice:: qalAdd4
   :author: Brad Miller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: listAdd
   :topics: Unit7-ArrayList/listAdd
   :from_source: F
   :answer_a: [1, 3, 2]
   :answer_b: [1, 3, 2, 1]
   :answer_c: [1, 1, 2, 3]
   :answer_d: [1, 2, 3]
   :correct: b
   :feedback_a: You can add duplicate objects to a list so this list will have two 1's.
   :feedback_b: The add method adds each object to the end of the list and lists can hold duplicate objects.
   :feedback_c: This would be true if the list was sorted as you add to it, but this is not true.
   :feedback_d: This would be true if the list was sorted and you couldn't add duplicate objects, but lists are not sorted and you can add duplicate objects.
   :pct_on_first: 0.95
   :total_students_attempting: 20
   :num_students_correct: 20.0
   :mean_clicks_to_correct: 1.15

   What will print when the following code executes?
   
   .. code-block:: java
   
      List<Integer> list1 = new ArrayList<Integer>();
      list1.add(1);
      list1.add(3);
      list1.add(2);
      list1.add(1);
      System.out.println(list1);