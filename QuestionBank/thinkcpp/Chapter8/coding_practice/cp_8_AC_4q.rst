.. activecode:: cp_8_AC_4q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter8
    :subchapter: coding_practice
    :topics: Chapter8/coding_practice
    :from_source: T
    :language: cpp

    Robots will naturally deplete their charge as they carry out tasks.
    Write a function called ``chargeRobot`` which takes a ``Robot`` as
    a parameter and charges the robot to 100 percent. Then output the statement
    "Robot ``name`` is fully charged!".
    ~~~~
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

    void chargeRobot (Robot& r) {
        // Write your implementation here.
    }

    int main() {
        Robot bob = { "Bob", "MKZ", 143, 65, "sweeping floors" };
        chargeRobot (bob);
        printRobotData (bob);  // Bob should now have 100 percent batter
    }
    ====
    void printRobotData (Robot r) {
        cout << r.name << " (" << r.model << " " << r.serialNumber
                << ") has " << r.batteryLevelPercentage
                << " percent battery and is currently executing the task \""
                << r.task << "\"" << endl;
    }