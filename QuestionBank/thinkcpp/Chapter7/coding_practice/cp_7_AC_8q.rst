.. activecode:: cp_7_AC_8q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter7
    :subchapter: coding_practice
    :topics: Chapter7/coding_practice
    :from_source: T
    :language: cpp
    :practice: T

    Write the function ``countVowels`` which takes a ``string input`` and returns
    the number of vowerls in the ``string``. Remember, 'a', 'e', 'i', 'o', and 'u'
    are vowels.
    ~~~~
    #include <iostream>
    using namespace std;

    int countVowels (string input) {
        // Write your implementation here.
    }

    int main() {
        cout << countVowels ("onomatopoeia") << endl;      // Should output 8
        cout << countVowels ("cysts") << endl;             // Should output 0
        cout << countVowels ("vowels") << endl;            // Should output 2
    }