.. activecode:: own_version_find_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter7
  :subchapter: own_version_find
  :topics: Chapter7/own_version_find
  :from_source: T
  :language: cpp
  :caption: Our own find function

  In the active code below, we are finding the number of ``'e'`` characters in
  the "Shepard" part of "German Shepard" using our function.
  Then we use the built-in ``find`` function to demonstrate how they work differently.
  ~~~~
  #include <iostream>
  using namespace std;

  int find (string s, char c, int i) {
      int length = s.length();
      while (i < length) {
          if (s[i] == c) {
              return i;
          }
          i = i + 1;
      }
      return -1;
  }

  int main() {
      string dog = "German Shepard";
      int start_shepard = 7;
      cout << find(dog, 'e', start_shepard) << endl;
      cout << dog.find('e') << endl;
  }