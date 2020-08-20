.. mchoice:: cond_rec_mc3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter4
    :subchapter: Exercises
    :topics: Chapter4/Exercises
    :from_source: T
    :pct_on_first: 0.5
    :total_students_attempting: 2
    :num_students_correct: 2.0
    :mean_clicks_to_correct: 2.0

    What is printed when the following code executes?
    
    ::
    
        int x = 34;
    
        if (32 < x) {
            cout << "It's Freezing!";
        }
        if (x < 40) {
            cout << "It's Cold!";
        }
        if (x > 65) {
            cout << "It's Warm!"'
        }
        else {
            cout << "It's Hot!";
        }
    
    -   ::
    
            It's Freezing!
    
        -   Take a closer look at the conditions and the way they
            are written in the program.
    
    -   ::
    
            It's Cold!
    
        -   Take a closer look at the conditions and the way they
            are written in the program.
    
    -   ::
    
            It's Freezing!
            It's Cold!
    
        -   You've identified some of the conditons that are met!
            Take another look at the *chain* of conditionals at the
            end!
    
    -   ::
    
            It's Freezing!
            It's Cold!
            It's Hot!
    
        +   These statements are quite contradicting, but that's exactly
            what the output would be if we ran this code.
    
    -   ::
    
            It's Hot!
    
        -   Take a closer look at the conditions and the way they
            are written in the program.