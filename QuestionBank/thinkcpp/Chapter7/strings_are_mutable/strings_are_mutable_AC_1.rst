.. activecode:: strings_are_mutable_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter7
  :subchapter: strings_are_mutable
  :topics: Chapter7/strings_are_mutable
  :from_source: T
  :language: cpp
  :caption: String are mutable

  The active code below changes the first letter in ``greeting`` to be
  ``'J'``.
  ~~~~
  #include <iostream>
  using namespace std;

  int main() {
      string greeting = "Hello, world!";
      greeting[0] = 'J';
      cout << greeting << endl;
  }