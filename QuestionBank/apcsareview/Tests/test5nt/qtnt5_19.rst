.. mchoice:: qtnt5_19
  :author: bmiller
  :difficulty: 3.0
  :basecourse: apcsareview
  :chapter: Tests
  :subchapter: test5nt
  :topics: Tests/test5nt
  :from_source: T
  :answer_a: 4
  :answer_b: 5
  :answer_c: 6
  :answer_d: 7
  :answer_e: 8
  :correct: b
  :feedback_a: i%2 -1 ==0 means "is this number odd". See http://tinyurl.com/AP19-Q27
  :feedback_b: i%2 -1 ==0 means "is this number odd". See http://tinyurl.com/AP19-Q27
  :feedback_c: i%2 -1 ==0 means "is this number odd". See http://tinyurl.com/AP19-Q27
  :feedback_d: i%2 -1 ==0 means "is this number odd". See http://tinyurl.com/AP19-Q27
  :feedback_e: i%2 -1 ==0 means "is this number odd". See http://tinyurl.com/AP19-Q27

  What will be the value of ``sum`` after the execution of code above?

  .. code-block:: Java

      int sum = 0;
      for(int i = 0; i < 3; i++)
      {
          if((i % 2) - 1 ==0)
              sum += 3;
          else
              sum++;
      }