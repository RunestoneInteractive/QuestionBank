.. mchoice:: qalm_10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ListBasics
   :subchapter: listMedMC
   :topics: ListBasics/listMedMC
   :from_source: T
   :answer_a: [5, 7, 8, 12]
   :answer_b: [5, 7, 8, 11, 12]
   :answer_c: [11, 5, 7, 8, 12]
   :answer_d: [5, 7, 8, 12, 11]
   :answer_e: [5, 7, 11, 8, 12]
   :correct: b
   :feedback_a: What about the 11?
   :feedback_b: This will add the value at the correct location in a list in ascending order.
   :feedback_c: This would be true if it was <code>numList.add(0, value)</code>
   :feedback_d: This would be true if the while loop was from 0 to one less than the size of the list.
   :feedback_e: This would be true if it was <code>numList.add(i-1, value)</code>

   Assume that ``numList`` has been initialized with the following Integer objects: [5, 7, 8, 12].  Which of the following shows the values in ``numList`` after a call to ``mystery(11)``?

   .. code-block:: java

     private List<Integer> numList;
     public void mystery(int value)
     {
         int i = 0;
         while (i < numList.size() && numList.get(i) < value)
         {
             i++;
         }
         numList.add(i, value);
     }