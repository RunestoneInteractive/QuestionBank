.. activecode:: fivethree
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter5
  :subchapter: boolfunctions
  :topics: Chapter5/boolfunctions
  :from_source: F
  :language: cpp
  :caption: Bool functions

  #include <iostream>
  #include <cmath>
  using namespace std;

   bool isSingleDigit (int x)
   {
     return (x >= 0 && x < 10);
   }

    int main ()
    {
      cout << isSingleDigit (2) << endl;
      bool bigFlag = !isSingleDigit (17);
      cout << bigFlag;
      return 0;
    }