.. activecode:: cp_7_AC_4q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter7
    :subchapter: coding_practice
    :topics: Chapter7/coding_practice
    :from_source: T
    :language: cpp
    :practice: T

    Write a void function ``removeWord`` that removes a given word from a given string and prints
    out the new string. ``removeWord`` should take two strings ``input`` and ``word`` as parameters
    and prints out ``input`` with every occurence of ``word`` removed. Use string concatenation and the C++
    string function ``substr``. ``substr`` takes two parameters, a starting index and a length. For example,
    if ``string greeting = "hello world"``, then ``greeting.substr(6, 5)`` returns the string ``"world"``.
    Test your function in main. The output should be:

    ::

        Gucci , Gucci , Gucci , Gucci
    ~~~~
    #include <iostream>
    using namespace std;

    void removeWord (string input, string word) {
        // Write your implementation here.
    }

    int main() {
        removeWord ("Gucci gang, Gucci gang, Gucci gang, Gucci gang", "gang");
    }