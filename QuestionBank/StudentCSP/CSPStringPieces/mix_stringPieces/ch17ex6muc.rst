.. parsonsprob:: ch17ex6muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPStringPieces
   :subchapter: mix_stringPieces
   :topics: CSPStringPieces/mix_stringPieces
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :pct_on_first: 0.1089108911
   :total_students_attempting: 101
   :num_students_correct: 63.0
   :mean_clicks_to_correct: 6.5079365079

   The following program segment should define and then call the function <i>storyTime</i> which uses variables to piece together a story. The blocks have been mixed up and include an extra block that isn't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   def storyTime(name, place, treasure):
   =====
       intro = "There once was an explorer named " + name
   =====
       middle = name + " was on a voyage to " + place
   =====
       end = name + " was traveling all this way in hopes of finding " + treasure
   =====
       print(intro)
   =====
       print(middle)
   =====
       print(end)
   =====
   storyTime("Indiana Jones", "Venice", "the Holy Grail")
   =====
   def storyTime(intro, middle, end): #distractor