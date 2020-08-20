.. mchoice:: functions_mc5
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter3
    :subchapter: Exercises
    :topics: Chapter3/Exercises
    :from_source: T
    :pct_on_first: 0.5
    :total_students_attempting: 2
    :num_students_correct: 2.0
    :mean_clicks_to_correct: 2.5

    What is printed when the following code runs?  Are there any errors?
    
    ::
    
        #include <iostream>
        using namespace std;
    
        void giveCompliment () {
            cout << "You are awesome!";
        }
    
        void giveInsult () {
            insult = "You suck!";
        }
    
        int main () {
            giveInsult ();
        }
    
    -   ``"You are awesome!"``
    
        -   The ``giveCompliment`` function is not called in ``main``.
    
    -   ``"You suck!"``
    
        -   The ``giveInsult`` function doesn't ``cout`` anything.
    
    -   Nothing is printed.
    
        +   Correct!  ``giveInsult`` doesn't ``cout`` anything.
    
    -   Error!
    
        -   There are no errors with this program!