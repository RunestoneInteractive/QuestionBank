.. parsonsprob:: question5_4_1p
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Functions
   :subchapter: TheAccumulatorPattern
   :topics: Functions/TheAccumulatorPattern
   :from_source: None

   Rearrange the code statements so that the program will add up the first n odd numbers where n is provided by the user.
   -----
   n = int(input('How many odd numbers would
   you like to add together?'))
   thesum = 0
   oddnumber = 1
   =====
   for counter in range(n):
   =====
      thesum = thesum + oddnumber
      oddnumber = oddnumber + 2
   =====
   print(thesum)