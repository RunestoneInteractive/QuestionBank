.. activecode:: multiple_assignment_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter6
  :subchapter: multiple_assignment
  :topics: Chapter6/multiple_assignment
  :from_source: T
  :language: cpp
  :caption: Multiple assignment

  The active code below reassigns ``fred`` from 5 to 7 and prints both values out.
  ~~~~
  #include <iostream>
  using namespace std;

  int main () {
      int fred = 5;
      cout << fred;
      fred = 7;
      cout << fred;
      return 0;
  }