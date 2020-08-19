.. mchoice:: cond_rec_mc8
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
    :mean_clicks_to_correct: 5.0

    Suppose you have defined the following function:
    
    ::
    
        void theThing (int m, int n, bool b) {
            if (b) {
                if (m % 4 == 0) {
                    cout << m;
                    return;
                }
                if ((m + n) > 10) {
                    cout << m + n;
                    return;
                }
            }
            else if ((m > n) == b) {
                cout << m - n;
                return;
            }
            else {
                if (n % 3 == 0) {
                    cout << n;
                    return;
                }
            }
            cout << -1;
        }
    
    What is printed when we run the following code?
    
    ::
    
        theThing (6, 4, true);
    
    -   6
    
        -   ``5 % 4 != 0`` in the ``if`` block, so the function doesn't print 6.
    
    -   10
    
        -   ``m + n !> 10`` in the ``if`` block, so the function doesn't print 10.
    
    -   2
    
        -   The condition for ``if`` is met, so the function never enters the ``else if``.
    
    -   4
    
        -   The condition for ``if`` is met, so the function never enters the ``else``.
    
    -   -1
    
        +   None of the conditions were met, so we reach the default cout -1.