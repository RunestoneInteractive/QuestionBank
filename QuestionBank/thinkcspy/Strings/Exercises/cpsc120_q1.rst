.. parsonsprob:: cpsc120_q1
   :author: Matthew Zuniga
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: Exercises
   :topics: Strings/Exercises
   :from_source: F
   
   Write a code snippet that uses a for loop to output all even numbers between 1 and 100. <br>
   Using the accumulator pattern, add these numbers and output the sum. <br>

   Assume all necessary #include statements and namespaces are already in the program.
   -----
   for(int i = 1; < 100; i++) {
    if(i % 2 == 0) {
     cout << i << endl;
    }
   }