.. mchoice:: functions_mc10
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter3
    :subchapter: Exercises
    :topics: Chapter3/Exercises
    :from_source: T
    :pct_on_first: 1.0
    :total_students_attempting: 2
    :num_students_correct: 2.0
    :mean_clicks_to_correct: 1.0

    How many local variables and parameters does ``mult`` have?
    
    ::
    
        void mult (int a, b, int c) {
            int d = 7;
            cout << a * b * c * d;
        }
    
    -   1 parameter, 3 local variables
    
        -   Remember, the parameters are declared in the function definition,
            and the local variables are declared *inside* of the function.
    
    -   2 parameters, 4 local variables
    
        -   You can declare multiple variables at once!  Also, remember that
            local variables are declared *inside* of the function.
    
    -   2 parameters, 1 local variables
    
        -   You can declare multiple variables at once!
    
    -   3 parameters, 1 local variable
    
        +   ``a``, ``b``, and ``c`` are parameters declared in the function
            definition. ``d`` is a local variable declared inside of the function.
    
    -   3 parameters, 4 local variables
    
        -   Remember that local variables are declared *inside* of the function.