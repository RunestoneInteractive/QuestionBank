.. parsonsprob:: visGeoload
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPWebData
   :subchapter: Exercises
   :topics: CSPWebData/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.0
   :total_students_attempting: 47
   :num_students_correct: 41.0
   :mean_clicks_to_correct: 7.5609756098

   Put the blocks in order to match the process in geoload.py.  There is one extra block that isn't needed in a correct solution.
   -----
   import libraries
   =====
   set up for the API and connect to the database
   open the file where.data
   set count to 0
   =====
   loop through the locations in where.data
   =====
       if count is more than 200 exit the program
   =====
       if count is more than 20 exit the program #distractor
   =====
       if the location is in the database continue
   =====
       Otherwise get the data from the API
   =====
           Store the data in the database
           Increment count
           Sleep if count % 10 is 0