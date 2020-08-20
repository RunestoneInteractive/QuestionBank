.. parsonsprob:: write-modified-Parsons
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameNames
   :subchapter: Exercises
   :topics: CSPNameNames/Exercises
   :from_source: F
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.3545816733
   :total_students_attempting: 251
   :num_students_correct: 250.0
   :mean_clicks_to_correct: 3.588

   Put the code in order to open the files and loop through the lines
   in the input file.  Each line has city, state: pm10: pm25.  
   Split each line at the ':' which gives you the 
   city and state together, pm10, and pm25.  Split the city and 
   state by the ',' to get the city and state.  Write out the 
   information to the output file as city state, pm10, pm25. Then
   close the files.
   -----
   inFile = open("uspoll.txt","r")
   outFile = open("poll.csv", "w")
   =====
   # each line has city, state: pm10: pm25
   for line in inFile:
   =====
       l1 = line.split(":")
   =====
       cityAndState = l1[0]
       pm10 = l1[1]
       pm25 = l1[2]
   =====
       l2 = cityAndState.split(",")
   =====
       city = l2[0]
       state = l2[1]
   =====
       outFile.write("%s %s, %s, %s" % (city, state, pm10, pm25))
   =====
   inFile.close()
   outFile.close()