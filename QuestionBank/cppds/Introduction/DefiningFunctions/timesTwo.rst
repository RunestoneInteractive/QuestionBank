.. activecode:: timesTwo
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cppds
  :chapter: Introduction
  :subchapter: DefiningFunctions
  :topics: Introduction/DefiningFunctions
  :from_source: T
  :language: cpp
  :caption: Implementation of the timesTwo function

  #include <iostream>
  using namespace std;

  int timesTwo(int num) {
      /* return type int which indicates
         that an integer is being returned */
      return num*2;
  }

  int main() {
      /* return type int which indicates that
         an integer is being returned */
      cout<<timesTwo(5)<<endl;

      return 0;
  }