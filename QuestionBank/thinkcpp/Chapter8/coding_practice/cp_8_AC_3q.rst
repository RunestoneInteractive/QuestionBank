.. activecode:: cp_8_AC_3q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter8
   :subchapter: coding_practice
   :topics: Chapter8/coding_practice
   :from_source: T
   :language: cpp
   :practice: T

   #include <iostream>
   using namespace std;

   struct Robot {
       // Write your implementation here.
   };

   void printRobotData (Robot r) {
       // Write your implementation here.
   }

   int main() {
       Robot rob = { "Rob", "XLV", 9800, 45, "washing dishes" };

       // Should output: Rob (XLV 9800) has 45 percent battery
       // and is currently executing the task "washing dishes".
       printRobotData (rob);
   }