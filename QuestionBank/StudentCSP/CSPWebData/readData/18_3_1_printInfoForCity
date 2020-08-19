.. parsonsprob:: 18_3_1_printInfoForCity
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPWebData
   :subchapter: readData
   :topics: CSPWebData/readData
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.2857142857
   :total_students_attempting: 455
   :num_students_correct: 387.0
   :mean_clicks_to_correct: 4.8397932817

   The following program prints the pollution information for all cities that start with a ``D``, but the code is mixed up.  Drag the blocks of statements from the left column to the right column and put them in the right order.  Then click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order or have the wrong indention.
   -----
   # open the file for reading
   inFile = open("uspoll.txt","r")
   
   # read a line from the file
   line = inFile.readline()
   =====
   # while there is another line
   while line:
   =====
       # split at the :
       v = line.split(":")
   
       # get the city
       city = v[0]
   =====
       # if city starts with an D print info
       if (city.find("D") == 0):
           print('City: ', city)
           print("Pollution values:",v[1],v[2])
   =====
       # read the next line
       line = inFile.readline()
   =====
   # close the file
   inFile.close()