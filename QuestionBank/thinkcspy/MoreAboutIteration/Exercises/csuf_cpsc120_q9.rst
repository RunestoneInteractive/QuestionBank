.. parsonsprob:: csuf_cpsc120_q9
   :author: Matthew Zuniga
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: MoreAboutIteration
   :subchapter: Exercises
   :topics: MoreAboutIteration/Exercises
   :from_source: F
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Similar with a for loop, we can use a <b>while loop> to use the <b>accumulator pattern.</b><br>
   <br>
   One of your colleagues is writing a program to find the <b>mean</b> (average) of their homework scores.<br>
   <br>
   Construct a program that solves this problem.
   
   -----
   int sum = 0;
   int counter = 4;
   vector&#60;int&#62 scores {90, 90, 100, 95, 85};
   =====
   while(counter >= 0) {
   =====
    sum += scores.at(counter);
    counter--;
   }
   int average = sum / 4;
   =====
   #distractorwhile(counter < 0) {
   =====
   #distractorwhile(counter != 0) {