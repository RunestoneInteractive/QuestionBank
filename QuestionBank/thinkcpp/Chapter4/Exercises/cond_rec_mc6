.. mchoice:: cond_rec_mc6
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
    
        void fortuneCookie (int a, bool b, char c) {
            if (c < 'm') {
                if (a % 2 == 0) {
                    cout << "An alien of some sort will be appearing to you shortly.";
                }
                else {
                    cout << "The fortune you seek is in another cookie.";
                }
            }
            else if (c < 'r') {
                if (b) {
                    cout << "He who laughs at himself never runs out of things to laugh at.";
                }
                else {
                    cout << "You will be hungry again in one hour.";
                }
            }
            else {
                cout << "Fortune not found? Abort, retry, ignore.";
            }
        }
    
    What will be your fortune if you run the following code?
    
    ::
    
        fortuneCookie(22, true, 'b');
    
    -   ``An alien of some sort will be appearing to you shortly.``
    
        +   ``'b' < 'm'`` and ``22 % 2 == 0``, so this is the fortune that will print.
    
    -   ``The fortune you seek is in another cookie.``
    
        -   ``22 % 2 == 0``, so you enter the ``if`` block, not the else.
    
    -   ``He who laughs at himself never runs out of things to laugh at.``
    
        -   ``'b'`` is less than ``'m'``, so you would enter the ``if`` block, not the ``else if``.
    
    -   ``You will be hungry again in one hour.``
    
        -   ``'b'`` is less than ``'m'``, so you would enter the ``if`` block, not the ``else if``.
    
    -   ``Fortune not found? Abort, retry, ignore.``
    
        -   ``'b'`` is less than ``'m'``, so you would enter the ``if`` block, not the ``else``.