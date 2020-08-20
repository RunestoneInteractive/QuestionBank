.. activecode:: traversal_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter7
  :subchapter: traversal
  :topics: Chapter7/traversal
  :from_source: T
  :language: cpp
  :caption: Accessing a string character

  The active code below outputs each letter of string ``fruit``
  using a while loop.
  ~~~~
  #include <string>
  #include <iostream>
  using namespace std;

  int main() {
      int index = 0;
      string fruit = "apple";
      int lengthfruit = fruit.length();
      while (index < lengthfruit) {
          char letter = fruit[index];
          cout << letter << endl;
          index = index + 1;
      }
  }