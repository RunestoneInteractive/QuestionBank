.. activecode:: find_function_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter7
  :subchapter: find_function
  :topics: Chapter7/find_function
  :from_source: T
  :language: cpp
  :caption: The find function

  Take a look at the active code below, which uses the ``find`` function to find
  the character ``'a'`` in string ``fruit`` and string ``dessert``.
  ~~~~
  #include <iostream>
  using namespace std;

  int main() {
      string fruit = "banana";
      int index = fruit.find('a');
      cout << index << endl;
      string dessert = "pudding";
      int another_index = fruit.find('a');
      cout << another_index << endl;
  }