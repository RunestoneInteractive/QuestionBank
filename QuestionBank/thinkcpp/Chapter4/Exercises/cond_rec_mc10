.. mchoice:: cond_rec_mc10
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter4
    :subchapter: Exercises
    :topics: Chapter4/Exercises
    :from_source: T
    :pct_on_first: 0.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 2.0

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
    
        moo (5, 10);
    
    -   0
    
        -   When we call the function ``5 != 10``, so "Moo!" is printed at least
            once.
    
    -   1
    
        -   The function calls itself inside of the ``if`` loop, so "Moo!" is printed
            more than once.
    
    -   2
    
        -   After two function calls, ``m == 9`` and ``n == 10``.  The function is not
            done printing.
    
    -   3
    
        -   After three function calls, ``m == 11`` and ``n == 10``.  The function is not
            done printing
    
    -   infinite recursion
    
        +   The function stops printing "Moo!" when ``m == n``, but since ``m`` is odd
            and ``n`` is even, they will never be equal as long as we increment by two.