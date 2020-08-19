.. parsonsprob:: count_subject-Parsons
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameNames
   :subchapter: Exercises
   :topics: CSPNameNames/Exercises
   :from_source: F
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.1490196078
   :total_students_attempting: 255
   :num_students_correct: 251.0
   :mean_clicks_to_correct: 7.3824701195

   Put the code in order to define a function that prints the 
   number of lines that begin with "Subject" in the passed file.
   It should try to open the file and if that causes an exception 
   it should print that it can't open the file and the file name
   and then exit the program.  Otherwise, it should set the count
   to zero and then loop through the lines in the file.  If the line 
   starts with 'Subject:' it should increment the count. After if 
   finishes reading the lines it should print the count and close the 
   file.
   -----
   def count_subject(fname):
   =====
       try:
   =====
           fhand = open(fname)
   =====
       except:
   =====
           print('File cannot be opened:', fname)
   =====
           exit()
   =====
       count = 0
   =====
       for line in fhand:
   =====
           if line.startswith('Subject:'):
   =====
               count = count + 1
   =====
       print('There were {} subject lines in {}'.format(count, fname))