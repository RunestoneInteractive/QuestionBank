.. mchoice:: qtnt5_7
      :author: bmiller
      :difficulty: 3.0
      :basecourse: apcsareview
      :chapter: Tests
      :subchapter: test5nt
      :topics: Tests/test5nt
      :from_source: T
      :answer_a: 10
      :answer_b: 12
      :answer_c: 16
      :answer_d: 26
      :answer_e: 32
      :correct: c
      :feedback_a: Trace out the recursive calls, see https://tinyurl.com/AP19-Q10
      :feedback_b: Trace out the recursive calls, see https://tinyurl.com/AP19-Q10
      :feedback_c: Trace out the recursive calls, see https://tinyurl.com/AP19-Q10
      :feedback_d: Trace out the recursive calls, see https://tinyurl.com/AP19-Q10
      :feedback_e: Trace out the recursive calls, see https://tinyurl.com/AP19-Q10

      Consider the following method. What will the output of ``mystery(6)`` return?

      .. code-block:: java

        public int mystery(int n)
        {
            if(n == 1 || n ==2)
                return 2;
            else
                return mystery(n -1) + mystery(n - 2);
        }