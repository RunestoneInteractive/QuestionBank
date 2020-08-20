.. mchoice:: qtnt1_16
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test1nt
   :topics: Tests/test1nt
   :from_source: T
   :answer_a: edcba
   :answer_b: edcb
   :answer_c: Nothing is printed because an IndexOutOfBoundsException is thrown.
   :answer_d: feeddccbba
   :answer_e: fededcdcbcba
   :correct: a
   :feedback_a: The substring method takes two arguments, a start index (which is inclusive) and an end index (which is exclusive). The first substring is from index 1 (counter + 1) to index 2 (counter + 2). However the second index is not included so its just index 1 which is e. We then simply keep getting every indidual element from the string one by one until the end of the string.
   :feedback_b: This substring is mostly correct but it ends early and is missing the a character at the end.
   :feedback_c: Even though the end of the substring is specified as index counter + 2, which will be past the end of the string the last time through the loop, substring doesn't include the value at the end index, so the code will execute.
   :feedback_d: The first substring element has a start value of index 1 and so f will not be printed out. Also because each substring is a single character, no character will be repeated in the substring.
   :feedback_e: This is what we would have happened if the substring had started at index counter (and not index counter + 1).


   Consider the following code segment. What will be printed as a result of executing the code below?

   .. code-block:: java

      String str = "fedcba";
      int counter = 0;
      while(counter < str.length() - 1)
      {
        System.out.print(str.substring(counter + 1, counter + 2));
        counter++;
      }