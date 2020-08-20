.. mchoice:: functEx_3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: Exercises
    :topics: 04-functions/Exercises
    :from_source: T
    :answer_a: value
    :answer_b: Second
    :answer_c: parameter
    :answer_d: First
    :correct: b
    :feedback_a: value is the name of a variable. This code will print what value is assigned to.
    :feedback_b: value is assigned to the parameter "Second", so that's what will print.
    :feedback_c: parameter will end up equalling the value sent with the function call.
    :feedback_d: Although, the variable value is assigned to "First" initially, it is reassigned to the parameter.

    What value is printed when the following code is executed?

    .. code-block:: python

        name = "John Smith"
        def myFunction(parameter):
            value = "First"
            value = parameter
            print (value)

        myFunction("Second")