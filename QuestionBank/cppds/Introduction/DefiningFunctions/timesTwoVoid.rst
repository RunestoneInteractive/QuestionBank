.. activecode:: timesTwoVoid
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cppds
  :chapter: Introduction
  :subchapter: DefiningFunctions
  :topics: Introduction/DefiningFunctions
  :from_source: T
  :language: cpp
  :caption: Implementation of the timesTwoVoid function

  #include <iostream>
  using namespace std;

  void timesTwoVoid(int num) {
    /* return type void which indicates
       that an nothing is being returned */
    cout<< num*2<<endl;
  }

  int main() {
      /* return type int which indicates that
         an integer is being returned */
      timesTwoVoid(5);

      return 0;
  }