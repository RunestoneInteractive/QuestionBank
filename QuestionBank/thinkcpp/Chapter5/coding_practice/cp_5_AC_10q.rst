.. activecode:: cp_5_AC_10q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter5
    :subchapter: coding_practice
    :topics: Chapter5/coding_practice
    :from_source: T
    :language: cpp
    :practice: T

    Write the function ``digitSum`` which takes an ``int num`` as a parameter
    and returns the sum of all its digits. For example, ``digitSum (1423)``
    would return 10. Use recursion.
    ~~~~
    #include <iostream>
    using namespace std;

    int digitSum (int num) {
        // Write your implementation here.
    }

    int main() {
        cout << digitSum (123) << endl;    // Should output 6
        cout << digitSum (8739) << endl;   // Should output 27
        cout << digitSum (440) << endl;    // Should output 8
        cout << digitSum (2) << endl;      // Should output 2
    }