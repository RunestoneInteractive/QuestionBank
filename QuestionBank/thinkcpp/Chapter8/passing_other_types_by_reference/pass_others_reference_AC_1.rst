.. activecode:: pass_others_reference_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter8
  :subchapter: passing_other_types_by_reference
  :topics: Chapter8/passing_other_types_by_reference
  :from_source: T
  :language: cpp

  The active code below uses the ``swap`` function. Run the active code
  for the output!
  ~~~~
  #include <iostream>
  using namespace std;

  void swap (int& x, int& y) {
      int temp = x;
      x = y;
      y = temp;
  }

  int main() {
      int i = 7;
      int j = 9;
      swap (i, j);
      cout << i << j << endl;
  }