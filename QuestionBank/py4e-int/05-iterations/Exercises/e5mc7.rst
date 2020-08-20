.. mchoice:: e5mc7
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 05-iterations
    :subchapter: Exercises
    :topics: 05-iterations/Exercises
    :from_source: T
    :practice: T
    :answer_a: var1 = -2, var2 = 0
    :answer_b: var1 = 0, var2 = -2
    :answer_c: var1 = 0, var2 = -1
    :answer_d: This is an infinite loop so it will never print anything.
    :correct: b
    :feedback_a: Try again! These are the initial values, but they change during the loop
    :feedback_b: Correct! This loop will execute two times so var1 will be 0 and var2 will be -2 after the loop finishes.
    :feedback_c: Try again! This would be true if the loop stopped executing as soon as var1 was equal to 0, but that isn't what happens. The body of the loop will finish executing before the value of var1 is tested again.
    :feedback_d: Try again! This would be true if it was var1 = var1 - 1.

    What are the values of var1 and var2 that are printed when the following code executes?

    ::

      output = ""
      var1 = -2
      var2 = 0
      while var1 != 0:
          var1 = var1 + 1
          var2 = var2 - 1
      print("var1: " + str(var1) + " var2 " + str(var2))