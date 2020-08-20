.. parsonsprob:: csuf_cpsc120_q2
   :author: Matthew Zuniga
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: MoreAboutIteration
   :subchapter: Exercises
   :topics: MoreAboutIteration/Exercises
   :from_source: F
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Now that you have written the code to output all the even numbers from 0 to 99, use the accumulator pattern to sum the even numbers up in a variable called int sum.
   
   -----
   int sum = 0;
   =====
   for(int i = 0; i < 100; i++) {
   ===== 
    if(i % 2 == 0) {
     sum += i;
    }
   =====
   }
   =====
   #distractorfor(int i = 1; i <= 99; i++) {
   =====