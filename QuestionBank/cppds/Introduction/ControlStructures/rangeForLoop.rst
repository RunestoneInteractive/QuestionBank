.. activecode:: rangeForLoop
  :author: Brad Miller
  :difficulty: 3.0
  :basecourse: cppds
  :chapter: Introduction
  :subchapter: ControlStructures
  :topics: Introduction/ControlStructures
  :from_source: F
  :language: cpp

  #include <iostream>
  using namespace std;

  int main() {
        for (int i=0; i<5; i++) {
          cout<<i*i<<endl;
      }

        return 0;
  }