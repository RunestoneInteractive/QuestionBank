.. mchoice:: qtnt4_10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test4nt
   :topics: Tests/test4nt
   :from_source: T
   :answer_a: [7, 2, 8, 1, 3, 5]
   :answer_b: [7, 8, 1, 6, 5, 3]
   :answer_c: [7, 2, 1, 3, 2, 5, 9]
   :answer_d: [7, 2, 8, 1, 6, 5, 9]
   :answer_e: [7, 2, 8, 1, 5]
   :correct: a
   :feedback_a: 8 is added at index 2, then index 4 is set to equal 1. The value at index 3 is removed, and 9 is added to the end of the array. Finally, the value at index 5 is set to equal 5.
   :feedback_b: Remember that for ArrayLists, indexing starts at 0, not 1.
   :feedback_c: When the add method has two parameters, the first parameter specifies the index and the second is the value to add at that index which moves any existing values to the right. The two parameters are not added to the end of the array.
   :feedback_d: The set method differs from the add method in that it replaces the original value at the specified index. The set method does NOT shift the numbers to the right of the specified index.
   :feedback_e: The add method adds the specified value at the specified index and shifts every index to the right of the current index. It does NOT delete the value at the original index.

   An ArrayList of integers ``numbers`` contains the values ``[7, 2, 4, 6, 3]``. What are the contents of ``numbers`` after the following code has been executed?

   .. code-block:: java

      numbers.add(2, 8);
      numbers.set(4, 1);
      numbers.remove(3);
      numbers.add(9);
      numbers.set(5, 5);