.. parsonsprob:: count_lines-Parsons
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPRepeatNumbers
   :subchapter: Exercises
   :topics: CSPRepeatNumbers/Exercises
   :from_source: F
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.1891891892
   :total_students_attempting: 259
   :num_students_correct: 259.0
   :mean_clicks_to_correct: 5.2239382239

   Put the code in order to define a function that returns a 
   count of the number of lines in the passed file.  It should
   set a count to 0 and open the file for reading.  Then it should 
   read a line from the file.  Next, it will loop while there is a valid line.
   In the loop it will increment the count of lines and read the next line.
   After the loop it will close the file and return the count.
   -----
   def count_lines(file):
   =====
       count = 0
       infile = open(file,"r")
   =====
       count = 0
       infile = open(file,"w") #paired
   =====
       line = infile.readline()
   =====
       line = infile.readLine() #paired
   =====
       while line:
   =====
       while line #paired
   =====
           count += 1
           line = infile.readline()
   =====
       infile.close()
   =====
       return count
   =====
       ret count #paired