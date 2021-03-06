.. mchoice:: qtnt2_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Tests
   :subchapter: test2nt
   :topics: Tests/test2nt
   :from_source: T
   :answer_a: [6, 2, 7, 5]
   :answer_b: [6, 4, 2, 7, 5]
   :answer_c: [4, 7, 9, 5]
   :answer_d: [6, 4, 7, 5]
   :answer_e: [4, 7, 6, 9, 5]
   :correct: d
   :feedback_a: When the add method is used with two parameters, the value is added at the specific index, not at the end of the list. In this list, 4 has been added at index 1.
   :feedback_b: This would be correct if 7 had been placed in the list using add, not set. Remember that the set method replaces the value at the index. It does not move the previous value to the right.
   :feedback_c: Remember that in ArrayLists, indexing starts at 0, not 1.
   :feedback_d: The 2 at index 1 is removed resulting in [6, 9], then a 4 is added at index 1 resulting in [6, 4, 9]. A 5 is added to the end of the list resulting in [6,4,9,5], and the value at 2 is replaced with a 7 resulting in [6,4,7,5].
   :feedback_e: Remember that in ArrayLists, indexing starts at 0, not 1. The set method replaces the value at the specified index with a new value, so the original value is deleted.

   Assume that ``list`` has been instantiated as an ArrayList of integers containing ``[6, 2, 9]`` . What are the contents of ``list`` after the code is executed?

   .. code-block:: java

      list.remove(2);
      list.add(1, 4);
      list.add(5);
      list.set(2, 7);