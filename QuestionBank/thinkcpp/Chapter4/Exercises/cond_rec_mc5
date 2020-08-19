.. mchoice:: cond_rec_mc5
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter4
    :subchapter: Exercises
    :topics: Chapter4/Exercises
    :from_source: T
    :pct_on_first: 0.0
    :total_students_attempting: 2
    :num_students_correct: 2.0
    :mean_clicks_to_correct: 4.0

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
    
        fortuneCookie(14, false, 'm'');
    
    -   ``An alien of some sort will be appearing to you shortly.``
    
        -   ``'m'`` is NOT less than ``'m'``, so you don't even enter the ``if`` block.
    
    -   ``The fortune you seek is in another cookie.``
    
        -   ``'m'`` is NOT less than ``'m'``, so you don't even enter the ``if`` block.
    
    -   ``He who laughs at himself never runs out of things to laugh at.``
    
        -   ``if (b)`` really means ``if (b == true)``.
    
    -   ``You will be hungry again in one hour.``
    
        +   ``'m' < 'r'`` is true and ``b == false``, so this is the fortune that will print.
    
    -   ``Fortune not found? Abort, retry, ignore.``
    
        -   ``'m'`` is less than ``'r'`` so you would enter the ``else if`` block, not the ``else``.