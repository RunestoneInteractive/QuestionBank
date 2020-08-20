.. mchoice:: qtnt1_15
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test1nt
   :topics: Tests/test1nt
   :from_source: T
   :answer_a: [0, 1, 2, 3, 5, 7]
   :answer_b: [0, 1, 4, 3, 5, 7]
   :answer_c: [0, 8, 3, 4, 5, 7]
   :answer_d: [0, 8, 4, 3, 5, 7]
   :answer_e: [5, 7, 0, 8, 4, 3]
   :correct: d
   :feedback_a: This is what the ArrayList will look like after the first two operations in the code.
   :feedback_b: This is what the ArrayList will look like before we set the element at index 1 to be 8.
   :feedback_c: This is what would have happened if we thought randomNum was actually 3 and we added the number 4 at the incorrect index.
   :feedback_d: After we add 5 and 7 to the end of the array we remove the element at index 2 (which was 2). Then we use the index we had previously obtained (also 2) to add a new element 4. This pushes the element already at that index (and the ones after it) one space to the right. Fianlly, we set the element at index 1 to be 8. This sets the value at index 1 to 8.
   :feedback_e: This is what we would have happened if we thought the add method would add elements to the beggining of the ArrayList and not the end.


   If randomList is an ``ArrayList`` of ``Integer`` objects and is initially set to {0, 1, 2, 3}, what will randomList look like after the following code is executed?

   .. code-block:: java

     randomList.add(5);
     randomList.add(7);
     int randomNum = randomList.get(2);
     randomList.remove(2);
     randomList.add(randomNum, 4);
     randomList.set(1, 8);