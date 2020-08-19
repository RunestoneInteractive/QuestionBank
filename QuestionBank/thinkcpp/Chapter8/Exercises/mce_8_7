.. mchoice:: mce_8_7
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter8
    :subchapter: Exercises
    :topics: Chapter8/Exercises
    :from_source: T
    :practice: T
    :pct_on_first: 1.0
    :total_students_attempting: 2
    :num_students_correct: 2.0
    :mean_clicks_to_correct: 1.0

    What is the value of ``r.batteryLevelPercentage`` when the code is done running?
    
    .. code-block:: cpp
    
      struct Robot {
        string name;
        int batteryLevelPercentage;
        bool isFullyCharged;
      };
    
      void chargeRobot (Robot& r) {
        if (r.batteryLevelPercentage + 50 > 100) {
          r.batteryLevelPercentage = 100;
          r.isFullyCharged = true;
        }
        else {
          r.batteryLevelPercentage = r.batteryLevelPercentage + 50;
        }
      }
    
      int main() {
        Robot r = { "Rob", 60, false };
        chargeRobot (r);
      }
    
    - 100
    
      + The ``Robot`` object is passed by reference to ``chargeRobot``, which caps the ``batteryLevelPercentage`` at 100.
    
    - 110
    
      - Take a closer look at the ``chargeRobot`` function.
    
    - 60
    
      - Is the ``Robot`` object passed by value or by reference to ``chargeRobot``?
    
    - 1
    
      - That is the final value of ``r.isFullyCharged``.