.. activecode:: strings_comparable_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter7
  :subchapter: strings_are_comparable
  :topics: Chapter7/strings_are_comparable
  :from_source: T
  :language: cpp
  :caption: Strings are comparable

  Take a look at the active code below, which checks to see if ``word`` is
  equal to ``"banana"``.
  ~~~~
  #include <iostream>
  using namespace std;

  int main() {
      word = "banana";
      if (word == "banana") {
          cout << "Yes, we have no bananas!" << endl;
      }
  }