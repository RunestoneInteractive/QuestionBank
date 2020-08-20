.. mchoice:: functions_mc1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter3
    :subchapter: Exercises
    :topics: Chapter3/Exercises
    :from_source: T
    :pct_on_first: 0.6666666667
    :total_students_attempting: 3
    :num_students_correct: 3.0
    :mean_clicks_to_correct: 1.3333333333

    You want to spice up your resume before the career fair, so you decide to
    update your GPA using the program below. What is the GPA that you will
    have on display for future employers?
    
    ::
    
        #include <iostream>
        using namespace std;
    
        int main() {
          double GPA = 3.52;
          int updatedGPA = int(GPA);
          cout << "GPA: " << updatedGPA;
        }
    
    -   ``3.0``
    
        -   Its correct to think that your GPA will be rounded down, but what
            else happens when you convert from ``int`` to ``double``?
    
    -   ``3``
    
        +   Converting to an ``int`` always rounds down to the nearest integer, so I do not
            recommend using type conversions to build your resume... especially if you're
            close to ``4.0``.
    
    -   ``4.0``
    
        -   Converting to an int *will* round yor GPA, but not in the direction
            that you were hoping for... what else happens when you convert from
            ``int`` to ``double``?
    
    -   ``4``
    
        -   Converting to an int *will* round yor GPA, but not in the direction
            that you were hoping for.
    
    -   Error!
    
        -   No errors here! Type conversions are perfectly legal in C++!