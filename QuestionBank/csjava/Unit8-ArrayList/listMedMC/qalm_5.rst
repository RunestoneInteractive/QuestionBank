.. mchoice:: qalm_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit8-ArrayList
   :subchapter: listMedMC
   :topics: Unit8-ArrayList/listMedMC
   :from_source: T
   :practice: T
   :answer_a: [1, 2, 3, 4, 5]
   :answer_b: [1, 4, 5]
   :answer_c: [1, 4, 3, 5]
   :answer_d: [2, 4, 5]
   :answer_e: [2, 4, 3, 5]
   :correct: b
   :feedback_a: This would be true if the code just added each integer at the end of the list.  But, that is not what it does.
   :feedback_b: The list is [1], then [1, 2], then [1], then [1, 3], then [1, 4], then [1, 4, 5].
   :feedback_c: This would be true if the <code>set</code> was an add.
   :feedback_d: This would be true it it was <code>remove(0)</code>.  Remember that it removes the object at the given index.
   :feedback_e: This would be true if the <code>set</code> was an add and if it was <code>remove(0)</code>.

   What is printed as a result of executing the following code segment?

   .. code-block:: java

     List<Integer> aList = new ArrayList<Integer>();
     aList.add(new Integer(1));
     aList.add(new Integer(2));
     aList.remove(1);
     aList.add(1, new Integer(3));
     aList.set(1, new Integer(4));
     aList.add(new Integer(5));
     System.out.println(list);