.. activecode:: anyBase
   :author: Michael Jones
   :difficulty: 5.0
   :basecourse: thinkcspy
   :chapter: PythonTurtle
   :subchapter: Exercises
   :topics: PythonTurtle/Exercises
   :from_source: F
   :caption: Decimal to Any Base
    
   Modify your Binary converter program to input a base value (2,8 or 16) and a decimal number which will then be converted to the specified base number
   ~~~~
   # Decimal to Binary converter by your name
   # Hint: this loop might help
   base = 2
   for exp in range(4,-1,-1):
      print(base**exp)