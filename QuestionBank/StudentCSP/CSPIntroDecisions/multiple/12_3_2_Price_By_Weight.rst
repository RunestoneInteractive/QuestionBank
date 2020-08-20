.. parsonsprob:: 12_3_2_Price_By_Weight
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPIntroDecisions
   :subchapter: multiple
   :topics: CSPIntroDecisions/multiple
   :from_source: T
   :practice: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.4344978166
   :total_students_attempting: 916
   :num_students_correct: 847.0
   :mean_clicks_to_correct: 3.7107438017

   The following program should calculate the total price, but the lines are mixed up.   The price is based on the weight.  Items that weigh less than 2 pounds should cost 1.5.  Items that weigh more than 2 pounds should cost 1.3.   Drag the blocks from the left and place them in the correct order on the right.  Be sure to also indent correctly! Click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order or have the wrong indention.</p>
   -----
   weight = 0.5
   numItems = 5
   if weight < 2:
   =====
       price = 1.50
   =====
   if weight >= 2:
   =====
       price = 1.30
   =====
   total = weight * price
   =====
   print(weight)
   print(price)
   print(total)