.. fillintheblank:: assess_question1_11_11_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Dictionaries
    :subchapter: Exercises
    :topics: Dictionaries/Exercises
    :from_source: T
    :practice: T

    In order to get the last line to print "success", what should the value *x* (in the last line) be?

    .. sourcecode:: python

        d = { 'work': 'success', 'success': 'failure', 'failure': 'money', 'time': 'work', 'industry': 'time'}
        print d[d[x]]

    -   :(^time$)|('time')|("time"): Good Work!  The word time with quotes around it is better as it indicates that you understand that we were referring to a literal string value.
        :industry: It prints "work".
        :work: It prints "failure".
        :success: It prints "money".
        :.*: Incorrect, try again.