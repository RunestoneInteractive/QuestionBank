.. parsonsprob:: question1_400_1
   :author: Sara Spiegel
   :difficulty: 1.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: Exercises
   :topics: Unit4-Iteration/Exercises
   :from_source: F
   :pct_on_first: 0.0789473684
   :total_students_attempting: 38
   :num_students_correct: 37.0
   :mean_clicks_to_correct: 5.7567567568

   The following puzzle has the correct code to <b>modify</b> an inputted String so that all a's removed, but the code is mixed up. Drag the blocks from the left area into the correct order in the right area. Click on the "Check Me" button to check your solution.
   -----
   String word = scan.nextLine();
   =====
   int index = 0;
   =====
   //while still an a in word
   while (word.indexOf("a") >=0){
     =====
     //Find the next index for an a
       index = word.indexOf("a");
     =====
     //Remove the a at index by concatenating
     //substring up to index and then the rest of the string.
     word = word.substring(0,index) +
            word.substring(index+1);
   =====
   } //end loop
   =====
   System.out.println(word);