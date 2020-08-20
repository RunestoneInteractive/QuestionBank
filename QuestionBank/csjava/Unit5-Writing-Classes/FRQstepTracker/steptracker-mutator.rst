.. mchoice:: steptracker-mutator
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit5-Writing-Classes/FRQstepTracker
   :from_source: T
   :answer_a: StepTracker tr = new StepTracker(1000)
   :answer_b: tr.addDailysteps(1000);
   :answer_c: tr.activeDays();
   :answer_d: tr.averageSteps();
   :correct: b
   :feedback_a: No, this is a call to the constructor.
   :feedback_b: Yes, addDailySteps(1000) is a mutator method that adds the steps given as a parameter to an instance variable that keeps track of the steps taken so far.
   :feedback_c: No, activeDays() is an accessor method that returns the number of active days.
   :feedback_d: No, averageSteps() is a complex accessor method that calculates and returns the average number of steps from the instance variable.

   Which of the following methods is a mutator method that changes the value of an instance variable?