.. activecode:: max25
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPWebData
   :subchapter: largestPoll
   :topics: CSPWebData/largestPoll
   :from_source: T
   :tour_1: "Structural tour"; 2: web3-line1; 3: web3-line2; 4: web3-line3; 7: web3-line5; 8: web3-line6; 11: web3-line7; 14: web3-line8; 17: web3-line9; 20: web3-line10; 23: web3-line11; 24: web3-line12; 27: web3-line13;
   :nocodelens:

   # read all the lines
   inFile = open("uspoll.txt","r")
   lines = inFile.readlines()
   inFile.close()

   # initialize the variables
   maxCity = ''
   max25 = 0

   # loop through the lines
   for line in lines:

       # split at :
       values = line.split(":")

       # get the PM 2.5 pollution
       new25 = float(values[2])

       # if current >  max
       if new25 > max25:

           # save the new max info
           maxCity = values[0]
           max25 = new25 # save the new maximum

   # print the largest PM 2.5 value
   print("Largest is ",max25," in ",maxCity)