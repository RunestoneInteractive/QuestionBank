.. activecode:: average25
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPWebData
   :subchapter: avgPoll
   :topics: CSPWebData/avgPoll
   :from_source: T
   :tour_1: "Structural tour"; 2-4: web5-line1-3; 7-8: web5-line5-6; 11: web5-line7; 14: web5-line8; 17: web5-line9; 20: web5-line10; 21: web5-line11; 24: web5-line13;
   :nocodelens:

   # read all the lines
   inFile = open("uspoll.txt","r")
   lines = inFile.readlines()
   inFile.close()

   # initialize the variables
   total25 = 0
   count = 1.0

   # loop through the lines
   for line in lines:

       # split at :
       values = line.split(":")

       # get the PM 2.5 pollution
       new25 = float(values[2])

       # add to the total and count
       total25 = total25 + new25
       count = count + 1

   # print the average PM 2.5 value
   print("Average PM 2.5 value is ",total25/count)