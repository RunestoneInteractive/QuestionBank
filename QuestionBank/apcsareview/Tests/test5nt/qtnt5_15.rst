.. mchoice:: qtnt5_15
    :author: bmiller
    :difficulty: 3.0
    :basecourse: apcsareview
    :chapter: Tests
    :subchapter: test5nt
    :topics: Tests/test5nt
    :from_source: T
    :answer_a: return 4 * n;
    :answer_b: return 8 * n;
    :answer_c: return 64 * n;
    :answer_d: return (int) Math.pow(n,4);
    :answer_e: return (int) Math.pow(n,8);
    :correct: e
    :feedback_a: 3 iterations of the loop and each loop does  n^2
    :feedback_b: 3 iterations of the loop and each loop does  n^2
    :feedback_c: 3 iterations of the loop and each loop does  n^2
    :feedback_d: 3 iterations of the loop and each loop does  n^2
    :feedback_e: Method basically does (n^2)^3 which is the same as n ^ 8

    Which of the following could replace the body of ``compute`` so it does the same thing.

    .. code-block:: Java

        public static int compute(int n)
        {
            for(int i = 1; i < 4; i++)
            {
                n *= n;
            }
            return n;
        }