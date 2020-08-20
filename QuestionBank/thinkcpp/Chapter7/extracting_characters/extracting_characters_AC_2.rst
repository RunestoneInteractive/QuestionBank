.. activecode:: extracting_characters_AC_2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter7
  :subchapter: extracting_characters
  :topics: Chapter7/extracting_characters
  :from_source: T
  :language: cpp
  :caption: Accessing a string character

  The active code below accesses the first character in string ``fruit``.
  ~~~~
  #include <iostream>
  using namespace std;

  int main() {
      string fruit = "banana";
      char letter = fruit[0];
      cout << letter << endl;
  }