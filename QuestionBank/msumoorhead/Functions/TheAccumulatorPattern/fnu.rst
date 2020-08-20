.. activecode:: fnu
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Functions
   :subchapter: TheAccumulatorPattern
   :topics: Functions/TheAccumulatorPattern
   :from_source: None

   def square(x):
       '''raise x to the second power'''
       runningtotal = 0
       for counter in range(x):
           runningtotal = runningtotal + x

       return runningtotal

   toSquare = 10
   squareResult = square(toSquare)
   print("The result of", toSquare, "squared is", squareResult)