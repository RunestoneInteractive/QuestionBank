.. activecode:: string_variables_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter7
  :subchapter: string_variables
  :topics: Chapter7/string_variables
  :from_source: T
  :language: cpp
  :caption: Creating a string variable

  In the active code below, the first line creates a ``string`` without
  giving it a value. The second line assigns it the string value ``"Hello,"``.
  The third line is a combined declaration and assignment, also called an initialization.
  ~~~~
  #include <iostream>
  using namespace std;

  int main() {
      string first;
      first = "Hello, ";
      string second = "world.";
  }