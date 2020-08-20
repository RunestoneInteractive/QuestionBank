.. activecode:: max10_answer
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPWebData
   :subchapter: largestPoll
   :topics: CSPWebData/largestPoll
   :from_source: T
   :nocodelens:

   inFile = open("uspoll.txt","r")
   lines = inFile.readlines()
   inFile.close()

   maxCity = ''
   max10 = 0 # initialize max10
   for line in lines:
       values = line.split(":")
       new10 = float(values[1]) # set the value for new10 to be the current PM 10 value
       if new10 > max10:
           maxCity = values[0]
           max10 = new10  # save the new maximum
   print("Largest PM 10 value is ",max10," in ",maxCity)