.. activecode:: average10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPWebData
   :subchapter: avgPoll
   :topics: CSPWebData/avgPoll
   :from_source: T
   :nocodelens:

   inFile = open("uspoll.txt","r")
   lines = inFile.readlines()
   inFile.close()

   # Create and initialize total10
   count = 1.0
   for line in lines:
       values = line.split(":")
       # get the current PM 10 value
       # add the current PM 10 value to the total in total10
       count = count + 1

   print("Average PM 10 value is ",total10/count)