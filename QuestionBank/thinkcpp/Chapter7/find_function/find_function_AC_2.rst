.. activecode:: find_function_AC_2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter7
  :subchapter: find_function
  :topics: Chapter7/find_function
  :from_source: T
  :language: cpp
  :caption: The find function

  The active code below finds the starting index of ``"nan"`` in ``fruit``.
  ~~~~
  #include <iostream>
  using namespace std;

  int main() {
      string fruit = "banana";
      int index = fruit.find("nan");
      cout << index;
  }