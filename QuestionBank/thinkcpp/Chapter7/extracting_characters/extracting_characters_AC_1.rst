.. activecode:: extracting_characters_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter7
  :subchapter: extracting_characters
  :topics: Chapter7/extracting_characters
  :from_source: T
  :language: cpp
  :caption: Accessing a string character

  Take a look at the active code below. We extract the character
  at index 1 from string ``fruit`` using ``[`` and ``]``.
  ~~~~
  #include <iostream>
  using namespace std;

  int main() {
      string fruit = "banana";
      char letter = fruit[1];
      cout << letter << endl;
  }