.. mchoice:: qalm_9
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: listMedMC
   :topics: Unit7-ArrayList/listMedMC
   :from_source: T
   :practice: T
   :answer_a: [4, 3, 2, 1, 0]
   :answer_b: [1, 2, 3, 4, 0]
   :answer_c: [0, 1, 2, 3, 4]
   :answer_d: [2, 3, 4, 0, 1]
   :answer_e: [4, 0, 1, 2, 3]
   :correct: c
   :feedback_a: This would be true if it was <code>numList.add(numList.size() - i, obj)</code>
   :feedback_b: This would be true if it was <code>mystery(1)</code>
   :feedback_c: Each value is removed one at a time and added to the end of the list which results in the same list.
   :feedback_d: This would be true if it was <code>mystery(2)</code>
   :feedback_e: This would be true if it was <code>mystery(4)</code>
   :pct_on_first: 0.3879310345
   :total_students_attempting: 1740
   :num_students_correct: 1679.0
   :mean_clicks_to_correct: 2.4568195354

   Assume that ``numList`` has been initialized with the following Integer objects: [0, 1, 2, 3, 4].  What is the value of ``numList`` after ``mystery(5)`` executes?
   
   .. code-block:: java
   
     private List<Integer> numList;
     public void mystery(int n)
     {
         for (int i = 0; i < n; i++)
         {
             Integer obj = numList.remove(0);
             numList.add(obj);
         }
     }