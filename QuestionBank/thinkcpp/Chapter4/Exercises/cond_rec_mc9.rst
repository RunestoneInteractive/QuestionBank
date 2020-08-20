.. mchoice:: cond_rec_mc9
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter4
    :subchapter: Exercises
    :topics: Chapter4/Exercises
    :from_source: T
    :pct_on_first: 1.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 1.0

    Suppose you have defined the following function:
    
    ::
    
        void moo (int m, int n) {
            if (m != n) {
                m += 2;
                cout << "Moo!";
                moo (m, n);
            }
            else {
                cout << "Got Milk?";
            }
        }
    
    How many times does "Moo!" print when we run the following?
    
    ::
    
        moo (4, 8);
    
    -   0
    
        -   When we call the function ``4 != 8``, so "Moo!" is printed at least
            once.
    
    -   1
    
        -   The function calls itself inside of the ``if`` loop, so "Moo!" is printed
            more than once.
    
    -   2
    
        +   ``m`` is incremented by two each with each function call, so after two
            ``m == n`` and the recursion stops.
    
    -   3
    
        -   Take a look at how ``m`` is incremented with each function call.
    
    -   infinite recursion
    
        -   The function stops printing "Moo!" when ``m == n``.