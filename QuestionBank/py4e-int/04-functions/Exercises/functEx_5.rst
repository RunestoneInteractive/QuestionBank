.. mchoice:: functEx_5
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: Exercises
    :topics: 04-functions/Exercises
    :from_source: T
    :practice: T
    :answer_a: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    :answer_b: 1, 2, 3, 5, 6, 7, 9, 10, 11
    :answer_c: 9, 10, 11, 1, 2, 3, 5, 6, 7
    :answer_d: 9, 10, 5, 6, 1, 2, 3, 6, 7, 10, 11
    :answer_e: 1, 5, 9, 10, 5, 6, 1, 2, 3, 6, 7, 10, 11
    :correct: e
    :feedback_a: Although Python typically processes lines in order from top to bottom, function definitions and calls are an exception to this rule.
    :feedback_b: Although Python typically processes lines in order from top to bottom, function definitions and calls are an exception to this rule.  Although this order skips blank lines, it still lists the lines of code in order.
    :feedback_c: This is close, in that Python will not execute the functions until after they are called, but there are two problems here.  First, Python does not know which lines are function definitions until it processes them, so it must at least process the function headers before skipping over the functions. Section, notice that line 10 involves a function call.  Python must execute the function square before moving on to line 11.
    :feedback_d: This is close, in that Python will not execute the functions until after they are called, but there is one problem here.  Python does not know which lines are function definitions until it processes them, so it must at least process the function headers before skipping over the functions.
    :feedback_e: Python starts at line 1, notices that it is a function definition and skips over all of the lines in the function definition until it finds a line that it no longer included in the function (line 5).  It then notices line 5 is also a function definition and again skips over the function body to line 9.  On line 10 it notices it has a function to execute, so it goes back and executes that function.  Notice that that function includes another function call. It returns from the function call and completes the assignment in line 6. Then it returns the result of line 7 and completes the assignment in line 10.  Finally, it will go to line 11 after the function square and the assignment are complete.

    Consider the following Python code. Which of the following best reflects the order in which these
    lines of code are processed in Python? Note that line numbers are included on the left.

    .. code-block:: python
        :linenos:

        def pow(b, p):
            y = b ** p
            return y

        def square(x):
            a = pow(x, 2)
            return a

        n = 5
        result = square(n)
        print(result)