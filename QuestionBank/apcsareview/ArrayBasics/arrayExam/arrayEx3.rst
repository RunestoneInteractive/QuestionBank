.. mchoice:: arrayEx3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ArrayBasics
   :subchapter: arrayExam
   :topics: ArrayBasics/arrayExam
   :from_source: T
   :answer_a: 1
   :answer_b: 2
   :answer_c: 3
   :answer_d: 4
   :answer_e: 5
   :correct: c
   :feedback_a: This would be true if the second loop only executed one time, but it executes for all values in x.
   :feedback_b: This would be true if there were only 2 distinct values in x.
   :feedback_c: This changes b[x[i]] to true and then counts the number of true in b.  Since x only has 3 distinct values in it the answer will be 3.
   :feedback_d: This would be true if there were 4 distinct values in x.
   :feedback_e: This would be true if it was ``b[i] = true`` instead of ``b[x[i]] = true``.

   What is the value of ``count`` after the following code has executed?

   .. code-block:: java

     int [] x = {1, 2, 3, 3, 3};
     boolean b[] = new boolean[x.length];
     for (int i = 0; i < b.length; i++)
        b[i] = false;
     for (int i = 0; i < x.length; i++)
        b[ x[i] ] = true;
     int count = 0;
     for (int i = 0; i < b.length; i++)
     {
        if (b[i] == true) count++;
     }