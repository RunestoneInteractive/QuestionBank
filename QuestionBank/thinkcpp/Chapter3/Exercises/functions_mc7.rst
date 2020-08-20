.. mchoice:: functions_mc7
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
    :mean_clicks_to_correct: 1.5

    What is printed when the following code runs?  Are there any errors?
    
    ::
    
        #include <iostream>
        using namespace std;
    
        void greeting (string name) {
            cout << "hello, " << name << "!";
        }
    
        void goodbye (string name) {
            greeting (name);
            cout << "!!";
        }
    
        int main () {
            string hannah = "Hannah";
            string anna = "Anna";
            string louise = hannah;
            hannah = anna;
            anna = louise;
            goodbye (anna);
        }
    
    -   ``hello, Hannah!!!``
    
        +   Correct!
    
    -   ``hello, anna!!!``
    
        -   The function ``couts`` the *value* of the variable ``anna`` not
            the variable name!
    
    -   ``hello, Anna!!!``
    
        -   Is ``"Anna"`` still the value of ``anna``?
    
    -   ``hello, Louise!``
    
        -   The ``goodbye`` function adds extra exclamation points.
    
    -   ``hello, Louise!!!``
    
        -   We assigned the valu eof ``louise`` to ``anna``.  Is ``"Louise"``
            the value of ``louise``?
    
    -   Error!
    
        -   There are no errors with this program!