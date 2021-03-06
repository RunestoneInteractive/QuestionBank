.. parsonsprob:: cpsc120_lab_q4
   :author: Matthew Zuniga
   :difficulty: 0.0
   :basecourse: cpp4python
   :chapter: Control_Structures
   :subchapter: Exercises
   :topics: Control_Structures/Exercises
   :from_source: F

   In computer science, the <b>Fibonacci Sequence</b> is an important problem for the concepts of recursion and memoization. These are introduced to you in later courses. <br> <br>
   The Fibonacci Sequence is also called the <b>Golden Ratio.</b> It is a mathematical principle thought to be harmonious. It is found in nature and art. Have you seen the Roman <i>Pantheon</i>? That was constructed with the Golden Ratio. How about the <i>Mona Lisa</i>? That too uses the Golden Ratio.<br> <br>
   The definition of the <b>Fibonacci Number</b> is a sequence where each successive number is the sum of the two previous numbers for all n > 1 where the F(0) = 0 and F(1) = 1. <br> <br>
   As an equation: <b>F(n) = F(n-1) + F(n-2)</b><br><br>
   The initial Fibonacci sequence where n=2 is:<br>
   F(0) = 0,<br>F(1) = 1,<br>F(2) = 1<br><br>
   To find the Fibonacci Sequence for n=3:<br>
   <b>F(3) = F(3-1) + F(3-2) = F(2) + F(1) <br>
   = 1 + 1 <br>
   = 2 </b> <br><br>

   <b>Now that you have an understanding of the Fibonacci Sequence, use the code blocks to construct the solution to the Fibonacci Sequence where n=3.</b><br>
   -----
   =====
   int f0 = 0;
   int f1 = 1;
   int fibNum = 0;
   =====
   for(int i = 2; i <= 3; i++) {
   ===== 
    fibNum = f0 + f1;
    f0 = f1;
    f1 = fibNum;
   =====
   }
   =====
   #distractorfor(int i = 2; i < 3; i++) {
   =====
   #distractorfor(int i = 0; i < 3; i++) {