.. activecode:: While3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPIntroDecisions
   :subchapter: noteWhileExits
   :topics: CSPIntroDecisions/noteWhileExits
   :from_source: T
   :tour_1: "Structural tour"; 1: InfiniteWhile-line1; 2: InfiniteWhile-line2; 3: InfiniteWhile-line3; 4: InfiniteWhile-line4; 5-6: InfiniteWhile-line5-6; 7: InfiniteWhile-line7;

   size = 0
   while 1 == 1:              # infinite loop
       if size >= 5:          # exit condition
           break              # explicit break
       size = size + 1        # loop body
       print(size)            # loop body
   print("Final value of size: " + str(size))