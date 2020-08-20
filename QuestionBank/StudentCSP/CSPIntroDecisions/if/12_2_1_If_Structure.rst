.. mchoice:: 12_2_1_If_Structure
  :author: bmiller
  :difficulty: 3.0
  :basecourse: StudentCSP
  :chapter: CSPIntroDecisions
  :subchapter: if
  :topics: CSPIntroDecisions/if
  :from_source: T
  :practice: T
  :answer_a: line 3
  :answer_b: line 4
  :correct: b
  :feedback_a: Line 3 will only execute when x is less than 3.
  :feedback_b: Execution continues at the next statement beyond the block following the <code>if</code> when the logical expression is false.
  :pct_on_first: 0.7635327635
  :total_students_attempting: 1053
  :num_students_correct: 1047.0
  :mean_clicks_to_correct: 1.2607449857

   Given the code below, what line executes after line 2 executes?
  
   ::
  
     x = 4
     if x < 3:
         print ("x is less than 3")
     print ("All done")