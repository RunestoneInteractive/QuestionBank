.. activecode:: min10_ex
   :author: bmiller
   :difficulty: 3.0
   :basecourse: StudentCSP
   :chapter: CSPWebData
   :subchapter: lowestPoll
   :topics: CSPWebData/lowestPoll
   :from_source: T
   :nocodelens:

   inFile = open("uspoll.txt","r")
   lines = inFile.readlines()
   inFile.close()

   minCity = ''
   min10 = 500
   for line in lines:
       values = line.split(":")
       # set the value for new10 to be the current PM 10 value
       if new10 < min10:
           # Save the minimum city and state
           # save the minimum PM 10 value
   print("Smallest PM 10 value is ",min10," in ",minCity)