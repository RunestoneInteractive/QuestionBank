.. parsonsprob:: cpsc120_q9
   :author: Matthew Zuniga
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Strings
   :subchapter: Exercises
   :topics: Strings/Exercises
   :from_source: F

   Sometimes, we unintentionally create infinite loops. That is, an exit condition for the loop is never reached. This type of infinite loop is called an Alderson loop (like Elliot Alderson from the hit TV series, Mr. Robot!) An Alderson Loop is when an exit condition is programmed but can never be reached.
   <br> <br>
   Can you identify why the exit condition is never reached?
   <br> <br>
   Use the code blocks that will fix this infinite loop. <br> <br>
   
   <b>bool sentinel = 1;
   <br> 
   int n = 0;
   <br> 
   int sum = 0; <br>
   while(sentinel) { <br>
   &emsp;cout << “Enter a number: “ << endl; <br>
   &emsp;cin >> n; <br>
   &emsp;n = 0; <br>
   &emsp;sum += n; <br>
   &emsp;if(sum > 100) { <br>
   &emsp;&emsp;sentinel = false; <br>
   &emsp;} <br>
   }</b> <br> 

   -----
   i = 0
   #distractor x
   for i in range(10):
       y = y + 1