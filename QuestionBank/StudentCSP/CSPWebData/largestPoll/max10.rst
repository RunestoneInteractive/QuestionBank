.. activecode:: max10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPWebData
   :subchapter: largestPoll
   :topics: CSPWebData/largestPoll
   :from_source: T
   :nocodelens:

   inFile = open("uspoll.txt","r")
   lines = inFile.readlines()
   inFile.close()

   maxCity = ''
   # initialize max10 here
   for line in lines:
       values = line.split(":")
       # set the value for new10 to be the current PM 10 value
       if new10 > max10:
           maxCity = values[0]
           # save the new maximum
   print("Largest PM 10 value is ",max10," in ",maxCity)