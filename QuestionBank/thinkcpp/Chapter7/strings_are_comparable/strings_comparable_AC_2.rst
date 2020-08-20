.. activecode:: strings_comparable_AC_2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter7
  :subchapter: strings_are_comparable
  :topics: Chapter7/strings_are_comparable
  :from_source: T
  :language: cpp
  :caption: Strings are comparable

  The active code below uses comparison operators to determine the ordering
  of ``word`` relative to ``"banana"``.
  ~~~~
  #include <iostream>
  using namespace std;

  int main() {

    string word = "Zebra";

    if (word < "banana") {
      cout << "Your word, " << word << ", comes before banana." << endl;
    } else if (word > "banana") {
      cout << "Your word, " << word << ", comes after banana." << endl;
    } else {
      cout << "Yes, we have no bananas!" << endl;
    }
  }