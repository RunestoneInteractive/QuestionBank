.. mchoice:: qlb_2_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: topic-4-1-while-loops
   :topics: Unit4-Iteration/topic-4-1-while-loops
   :from_source: F
   :practice: T
   :answer_a: 5 4 3 2 1
   :answer_b: -5 -4 -3 -2 -1
   :answer_c: -4 -3 -2 -1 0
   :correct: c
   :feedback_a: x is initialized (set) to -5 to start.
   :feedback_b: x is incremented (x++) before the print statement executes.
   :feedback_c: x is set to -5 to start but then incremented by 1 so it first prints -4.

   What does the following code print? (To trace through the code, keep track of the variable x and its value, the iteration of the loop, and the output every time through the loop.)

   .. code-block:: java

     int x = -5;
     while (x < 0)
     {
        x++;
        System.out.print(x + " ");
     }