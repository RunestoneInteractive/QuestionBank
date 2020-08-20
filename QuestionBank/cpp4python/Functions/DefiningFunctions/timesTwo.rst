.. activecode:: timesTwo
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cpp4python
  :chapter: Functions
  :subchapter: DefiningFunctions
  :topics: Functions/DefiningFunctions
  :from_source: T
  :language: cpp
  :caption: Implementation of the timesTwo function

  #include <iostream>
  using namespace std;

  // function that multiplies a number by 2
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