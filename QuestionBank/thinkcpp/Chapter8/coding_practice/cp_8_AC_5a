.. activecode:: cp_8_AC_5a
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

   void printRobotData (Robot r);

   void resetRobot(Robot& r) {
       Robot reset = { "EnterAName", r.model, r.serialNumber, 100, "Idle" };
       r = reset;
   }

   int main() {
       Robot a = { "Bot", "RSO", 1985, 32, "gardening" };
       resetRobot (a);
       printRobotData (a);  // Bot should be reset
   }
   ====
   void printRobotData (Robot r) {
        cout << r.name << " (" << r.model << " " << r.serialNumber
             << ") has " << r.batteryLevelPercentage
             << " percent battery and is currently executing the task \""
             << r.task << "\"" << endl;
   }