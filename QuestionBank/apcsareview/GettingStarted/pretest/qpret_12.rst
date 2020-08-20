.. mchoice:: qpret_12
    :author: bmiller
    :difficulty: 3.0
    :basecourse: apcsareview
    :chapter: GettingStarted
    :subchapter: pretest
    :topics: GettingStarted/pretest
    :from_source: T
    :answer_a: Hi There
    :answer_b: hi there
    :answer_c: HI THERE
    :answer_d: null
    :answer_e: hI tHERE
    :correct: a
    :feedback_a: Strings are immutable meaning that any changes to a string creates and returns a new string, so the string referred to by s1 does not change
    :feedback_b: This would only be correct if we had s1 = s2; after s2.toLowerCase(); was executed. Strings are immutable and so any change to a string returns a new string.
    :feedback_c: This would be correct if we had s1 = s3; after s3.toUpperCase(); was executed. Strings are immutable and so any change to a string returns a new string.
    :feedback_d: This would be true if we had s1 = s4; after s4 = null; was executed. Strings are immutable and so any changes to a string returns a new string.
    :feedback_e: Strings are immutable and so any changes to a string returns a new string.

    Given the following code segment, what will the value of ``s1`` be after this executes?

    .. code-block:: java

        String s1 = "Hi There";
        String s2 = s1;
        String s3 = s2;
        String s4 = s1;
        s2 = s2.toLowerCase();
        s3 = s3.toUpperCase();
        s4 = null;