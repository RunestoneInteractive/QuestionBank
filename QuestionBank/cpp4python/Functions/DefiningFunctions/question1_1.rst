.. mchoice:: question1_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: Functions
    :subchapter: DefiningFunctions
    :topics: Functions/DefiningFunctions
    :from_source: T
    :multiple_answers:
    :answer_a: func2 is a pass-by-reference function, meaning that the values passed into the function are the direct memory references of the original variables.
    :answer_b: func1 is a pass-by-reference function, meaning that the values passed into the function are the direct memory references of the original variables.
    :answer_c: func1 is a pass-by-value value function, meaning that the values passed into the function are copies of the original variables.
    :answer_d: func2 is a pass-by-value value function, meaning that the values passed into the function are copies of the original variables.
    :correct: a, c
    :feedback_a: Correct!
    :feedback_b: No, func1 is simply using copies of the original variables as input because it is not using "&."
    :feedback_c: Correct!
    :feedback_d: No, func2 is using the direct memory references of the original variables because its input parameters are using "&."

    What is the difference between **func1** and **func2**? Check all that apply.