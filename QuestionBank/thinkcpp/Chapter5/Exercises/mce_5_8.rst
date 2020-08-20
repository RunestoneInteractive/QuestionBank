.. mchoice:: mce_5_8
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter5
    :subchapter: Exercises
    :topics: Chapter5/Exercises
    :from_source: T
    :practice: T
    :pct_on_first: 0.5
    :total_students_attempting: 2
    :num_students_correct: 2.0
    :mean_clicks_to_correct: 2.0

    Are there any issues with the code below?
    
    .. code-block:: cpp
    
      void moonWeight (double earth) {
        double moon = 0.165 * earth;
        cout << "You would weigh " << moon << " pounds on the moon." << endl;
        return moon;
      }
    
    - Yes, we cannot have ``cout`` statements in a function.
    
      - We are allowed to use ``cout`` statements in a function.
    
    - Yes, we cannot return anything in a ``void`` function.
    
      + ``void`` functions do not have return values, so we cannot return ``moon``.
    
    - Yes, we need to return the output statement.
    
      - ``void`` functions do not have return values.
    
    - There are no issues with the code.
    
      - There is an issue with the code. Can you find it?