.. parsonsprob:: cpsc120_lab_q5
   :author: Matthew Zuniga
   :difficulty: 0.0
   :basecourse: cpp4python
   :chapter: Control_Structures
   :subchapter: Exercises
   :topics: Control_Structures/Exercises
   :from_source: F

   There is a famous coding interview question called "Fizz Buzz". Fizz Buzz can be implemented using a simple for loop with many different if checks. <br> <br>
   The <b>pseudocode</b> of Fizz Buzz looks like this:<br><br>
   for i = 1 to i = 100 <br>
   if n is divisible by 3 and n is divisible by 5<br>
   &emsp;print "Fizz Buzz"<br>
   else if n is divisible by 3 <br>
   &emsp;print "Fizz" <br>
   else if n is divisible by 5 <br>
   &emsp;print "Buzz"<br>
   else print n<br>
   end if <br><br>

   Construct a solution to the Fizz Buzz problem using the code blocks.
   
   -----
   for(int i = 1; i < 100; i++) {
   =====
    if(i % 3 == 0 && i % 5 == 0) {
     cout << "Fizz Buzz" << endl;
    }
   =====
    else if(i % 3 == 0) {
     cout << "Fizz" << endl;
    }
   =====
    else if(i % 5 == 0) {
     cout << "Buzz" << endl;
    }
   =====
    else cout << i << endl;
   =====
   }
   =====