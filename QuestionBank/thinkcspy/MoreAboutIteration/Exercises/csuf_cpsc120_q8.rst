.. parsonsprob:: csuf_cpsc120_q8
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

   As with the <b>Fibonacci Sequence</b>, the <b>factorial problem</b> is another important problem in computer science. It can be done using recursion which again, will be taught in later courses.</b><br>
   <br>
   
   A factorial, <b>n!</b> is the product of all positive integers less than or equal to n. <br>
   <br>
   For example: 4! = 4 * 3 * 2 * 1 = 24
   <br>
    
   Using a <b>while loop</b>, create a program that calculates the factorial of a number.
   -----
   int val = 0;
   int i = 1;
   int factorial = 1;
   =====
   cout << "Enter a positive integer: " << endl;
   cin >> val;
   =====
   while(i <= val) {
    factorial *= i;
    i++;
   }
   =====
   cout << val << "! is: " << factorial << endl;
   =====
   #distractorwhile(i >= val) {