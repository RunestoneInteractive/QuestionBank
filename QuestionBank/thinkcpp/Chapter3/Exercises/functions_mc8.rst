.. mchoice:: functions_mc8
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

    **Multiple Response** Which of the following are legal function
    calls of ``orderFood``?
    
    ::
    
        #include <iostream>
        using namespace std;
    
        void orderFood (string food, int quantity) {
            cout << "I'll have " << quantity << " " << food;
        }
    
        int main () {
            string a = "wings";
            string b = "sliders";
            int c = 3;
            double d = 8.64;
            char e = 'p';
        }
    
    -   ``orderFood(a, c);``
    
        +   Correct!
    
    -   ``orderFood(b, d);``
    
        +   Correct!  Automatic type conversion will convert d to
            an ``int``.
    
    -   ``orderFood(e, c);``
    
        -   ``e`` has a character value, and this function takes a *string*.
    
    -   ``orderfood(a, d);``
    
        +   Correct! Automatic type conversion will convert d to
            an ``int``.
    
    -   ``orderFood(c, a);``
    
        -   You have to input your arguments in the correct order.