.. parsonsprob:: alt_execution_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter4
   :subchapter: AlternativeExecution
   :topics: Chapter4/AlternativeExecution
   :from_source: T
   :adaptive: 
   :pct_on_first: 0.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 2.0

   Construct a block of code that correctly goes through alternative
   execution for pricing of an entre at a nice restaurant.  If the
   price is more than $30.00, print "Expensive!".  If the price is
   less than $30.00, print "Inexpensive!"  You should by initializing
   the cost to $40.
   -----
   int cost = 40;
   
   if (cost > 30) {
   
   if (cost > 30) #distractor
   
    cout << "Expensive!";
   
   } //"if" bracket
   
   else {
   
   else if { #distractor
   
    cout << "Inexpensive!" #distractor
   
    cout << "Inexpensive!";
   
   } //"else" bracket