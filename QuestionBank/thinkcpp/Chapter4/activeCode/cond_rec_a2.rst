.. activecode:: cond_rec_a2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter4
    :subchapter: activeCode
    :topics: Chapter4/activeCode
    :from_source: T
    :language: cpp

    You are part of a class where everyone passes, but it's very hard
    to pass with an A.  Fix the function so it prints your letter grade
    according to this scheme.  [0, 50) = C, [50, 85) = B, and [85, 100] = A.
    ~~~~
    #include <iostream>
    using namespace std;

    string whichDoor (double grade) {
        s = "";
        if (grade < 50) {
            s = "C";
        }
        if (grade < 85) {
            s = "B";
        }
        if (grade >= 85) {
            s = "A";
        }
        cout << s;
    }