.. activecode:: rangeForLoop1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: cpp4python
   :chapter: Control_Structures
   :subchapter: for_loop
   :topics: Control_Structures/for_loop
   :from_source: T
   :language: cpp

   #include <iostream>
   using namespace std;

    // squares the numebers in range 5
    // ex. 0*0, 1*1, 2*2 ...
    int main() {
        for (int i=0; i<5; i++) {
            cout << i*i << " ";
        }

        return 0;
    }