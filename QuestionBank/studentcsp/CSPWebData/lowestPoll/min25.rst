.. activecode:: min25
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPWebData
   :subchapter: lowestPoll
   :topics: CSPWebData/lowestPoll
   :from_source: T
   :tour_1: "Structural tour"; 2-4: web4-line1-3; 7-8: web4-line5-6; 11: web4-line7; 14: web4-line8; 17: web4-line9; 20: web4-line10; 23-24: web4-line11-12; 27: web4-line13;
   :nocodelens:

   # read all the lines
   inFile = open("uspoll.txt","r")
   lines = inFile.readlines()
   inFile.close()

   # initialize the variables
   minCity = ''
   min25 = 500

   # loop through the lines
   for line in lines:

       # split at :
       values = line.split(":")

       # get the PM 2.5 pollution
       new25 = float(values[2])

       # if current <  min
       if new25 < min25:

           # save new min info
           minCity = values[0]
           min25 = new25

   # print the smallest PM 2.5 value
   print("Smallest PM 2.5 ",min25," in ",minCity)