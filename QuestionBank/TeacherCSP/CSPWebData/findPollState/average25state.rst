.. activecode:: average25state
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPWebData
   :subchapter: findPollState
   :topics: CSPWebData/findPollState
   :from_source: T
   :tour_1: "Structural tour"; 2-4: state3-line1-3; 7-9: state3-line5-7; 12: state3-line8; 15: state3-line9; 18: state3-line10; 21: state3-line11; 24: state3-line12; 25: state3-line13; 28: state3-line14; 31: state3-line16;
   :nocodelens:

   # read all the lines
   infile = open("uspoll.txt","r")
   lines = infile.readlines()
   infile.close()

   # initialize the variables
   state = "CA"
   total25 = 0
   count = 1.0

   # loop through the lines
   for line in lines:

       # split at :
       values = line.split(":")

       # split at ,
       cityState = values[0].split(",")

       # if found state
       if cityState[1].find(state) >= 0:

           # add the current to the sum
           new25 = float(values[2])
           total25 = total25 + new25

           # increment the count
           count = count + 1

   # print the average
   print("Average PM 2.5 value for " , state, " is ", total25/count)