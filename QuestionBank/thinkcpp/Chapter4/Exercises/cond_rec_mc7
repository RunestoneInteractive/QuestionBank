.. mchoice:: cond_rec_mc7
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
    
        theThing (5, 10, false);
    
    -   5
    
        -   The outer ``if`` condition is not met, the block does not execute.
    
    -   15
    
        -   The outer ``if`` condition is not met, the block does not execute.
    
    -   -5
    
        +   ``m > n`` evaluates to false, so the ``else if`` block executes.
    
    -   10
    
        -   The condition for ``else if`` is met, so the function never enters the ``else``.
    
    -   -1
    
        -   The function has returned.