.. parsonsprob:: max_poll2-Parsons
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPNameNumbers
   :subchapter: Exercises
   :topics: CSPNameNumbers/Exercises
   :from_source: F
   :numbered: left
   :practice: T
   :adaptive: 
   :pct_on_first: 0.2380952381
   :total_students_attempting: 252
   :num_students_correct: 248.0
   :mean_clicks_to_correct: 4.9475806452

   Put the code in order to find and print the city with the 
   most 2.5 pollution.  It should
   first open the file, read all the lines, and close the file.
   Next it should initialize the city with the maximum 
   pollution to the empty string and the max25 to zero.  Then
   it should loop through all the lines and split them at the 
   ':'.  It should get the 2.5 pollution for the line 
   and if that is greater than the max25 it should save the
   new values.  After the loop it should print the city
   with the most 2.5 pollution and the amount of pollution.
   -----
   file = open("uspoll.txt", "r")
   lines = file.readlines()
   file.close()
   =====
   max_city = ''
   max25 = 0
   =====
   for line in lines:
   =====
       values = line.split(":")
   =====
       new25 = float(values[2])
   =====
       if new25 > max25:
   =====
           max_city = values[0]
           max25 = new25
   =====
   print("The city with the most 2.5 pollution is: {} with {}".format(max_city, max25))