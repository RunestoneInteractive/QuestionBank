.. activecode:: printData
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPWebData
   :subchapter: readData
   :topics: CSPWebData/readData
   :from_source: T
   :tour_1: "Structural tour"; 2: web1-line4; 5: web1-line5; 8: web1-line6; 11: web1-line7; 14: web1-line8; 17: web1-line9; 18-19: web1-line10-11; 22: web1-line12; 25: web1-line14;
   :nocodelens:

   # open the file for reading
   inFile = open("uspoll.txt","r")

   # read a line from the file
   line = inFile.readline()

   # while there is another line
   while line:

       # create a list by splitting at the :
       values = line.split(":")

       # get the city from the list
       city = values[0]

       # if the city starts with an A print the info
       if (city.find("A") == 0):
           print('City: ', city)
           print("Pollution values:",values[1],values[2])

       # read the next line
       line = inFile.readline()

   # close the file
   inFile.close()