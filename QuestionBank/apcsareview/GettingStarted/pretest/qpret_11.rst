.. mchoice:: qpret_11
    :author: bmiller
    :difficulty: 3.0
    :basecourse: apcsareview
    :chapter: GettingStarted
    :subchapter: pretest
    :topics: GettingStarted/pretest
    :from_source: T
    :answer_a: 4
    :answer_b: 2
    :answer_c: 16
    :answer_d: 7
    :answer_e: 3
    :correct: b
    :feedback_a: This would be true if it was return (a[1] *= 2);
    :feedback_b: The statement a[1]--; is the same as a[1] = a[1] - 1; so this will change to 3 to 2.  The return (a[1] * 2) does not change the value at a[1].
    :feedback_c: This would be true if it was return (a[0] *= 2);
    :feedback_d: This would be true if it was a[0]--;
    :feedback_e: This can't be true because a[1]--; means the same as a[1] = a[1] - 1; so the 3 changes to 2.  Parameters are all pass by value in Java which means that a copy of the value is passed to a method. But, since an array is an object a copy of the value is a copy of the reference to the object. So changes to objects in methods are permanent.

    Given the following method declaration, and ``int[] a = {8, 3, 1}``, what is the value in ``a[1]`` after ``m1(a);`` is run?

    .. code-block:: java

        public static int m1(int[] a)
        {
           a[1]--;
           return (a[1] * 2);
        }