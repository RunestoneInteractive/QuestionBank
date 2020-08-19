.. activecode:: cp_8_AC_3a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter8
   :subchapter: coding_practice
   :topics: Chapter8/coding_practice
   :from_source: T
   :language: cpp
   :optional:

   #include <iostream>
   using namespace std;

   struct Robot {
       string name;
       string model;
       int serialNumber;
       int batteryLevelPercentage;
       string task;
   };

   void printRobotData (Robot r) {
        cout << r.name << " (" << r.model << " " << r.serialNumber
             << ") has " << r.batteryLevelPercentage
             << " percent battery and is currently executing the task \""
             << r.task << "\"" << endl;
   }

   int main() {
       Robot rob = { "Rob", "XLV", 9800, 45, "washing dishes" };

       // Should output: Rob (XLV 9800) has 45 percent battery
       // and is currently executing the task "washing dishes".
       printRobotData (rob);
   }