.. mchoice:: functions_mc6
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

    Rachel and Monica are best friends.  They write a function
    called ``bestFriends`` so that they announce this fact to the
    rest of their friends.  What is printed when they run the code
    below? Are there any errors?
    
    ::
    
        #include <iostream>
        using namespace std;
    
        void bestFriends (string a, string b) {
            cout << a << " is best friends with " << b;
        }
    
        int main () {
            string a = "Rachel";
            string b = "Monica";
            bestFriends(b, a);
        }
    
    -   ``"Monica is best friends with Rachel"``
    
        +   Correct!
    
    -   ``"Rachel is best friends with Monica"``
    
        -   You seem to be confusing your arguments and parameters!
    
    -   ``a is best friends with b``
    
        -   The function ``couts`` the *values* of the variables, not their
            names!
    
    -   ``b is best friends with a``
    
        -   The function ``couts`` the *values* of the variables, not their
            names!
    
    -   Error!
    
        -   There are no errors with this program!