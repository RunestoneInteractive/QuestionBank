.. mchoice:: qtnt5_12
    :author: bmiller
    :difficulty: 3.0
    :basecourse: apcsareview
    :chapter: Tests
    :subchapter: test5nt
    :topics: Tests/test5nt
    :from_source: T
    :answer_a: It prints string str
    :answer_b: It prints string str in reverse order
    :answer_c: It prints only the first two characters of string str
    :answer_d: It prints only the first two characters of string str
    :answer_e: It prints only the last character of string str
    :correct: a
    :feedback_a: Prints out the leftmost character at the start of the recursive call. Then always trims off the left most character, but substring(x) with single parameter x gives the remaining string from index x until the end. See https://tinyurl.com/AP19-Q17
    :feedback_b: substring(0,1) prints leftmost char not the rightmost char
    :feedback_c: there is a recursive call of a substring at each iteration
    :feedback_d: goes until s.length > 0
    :feedback_e: goes until s.length > 0 and there are recursive calculates

    Which best describes what the ``printSomething`` method below does?

    .. code-block:: Java

      public void printSomething(String str)
      {
          if(str.length() > 0)
          {
              System.out.print(str.substring(0,1));
              printSomething(str.substring(1));
          }

      }