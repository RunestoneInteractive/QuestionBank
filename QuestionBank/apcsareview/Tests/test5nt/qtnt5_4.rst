.. mchoice:: qtnt5_4
  :author: bmiller
  :difficulty: 3.0
  :basecourse: apcsareview
  :chapter: Tests
  :subchapter: test5nt
  :topics: Tests/test5nt
  :from_source: T
  :answer_a: -4
  :answer_b: 4
  :answer_c: 6
  :answer_d: 8
  :answer_e: -6
  :correct: c
  :feedback_a: Trace out the recursive calls. See https://tinyurl.com/AP19-Q6
  :feedback_b: Trace out the recursive calls. See https://tinyurl.com/AP19-Q6
  :feedback_c: Trace out the recursive calls
  :feedback_d: Trace out the recursive calls. See https://tinyurl.com/AP19-Q6
  :feedback_e: Trace out the recursive calls. See https://tinyurl.com/AP19-Q6

  Suppose methods ``f1`` and ``f2`` are defined as follows. What value is returned from the call ``f1(5)``?

  .. code-block:: java

    public int f1(int x)
    {
        if(x == 0)
            return 0;
        else
            return f2(x -2);
    }

    public int f2(int x)
    {
        if(x == 1)
            return 1;
        else
            return f1(x + 1) + x;
    }