.. activecode:: hw17bDE
   :author: Damon Ellingston
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: PythonTurtle
   :subchapter: Exercises
   :topics: PythonTurtle/Exercises
   :from_source: F

   **Homework 17 part b: histogram**
  
    Write a script that will sum up 2 simultaneous dice rolls and keep track of 1000 of those sums. The script will then draw a histogram (bar chart) indicating how many times it rolled each possible sum (2, 3, 4...11, 12). Create a data list using a for loop with 1,000 iterations. Then calculate the number of occurrences for each outcome (2, 3, 4...11, 12) using the List.count(n) method. 

    There will be two outputs to your code. First will be a histogram - see section 4.5 Graphing Future Value in Zelle for more details. Second will be a list with 11 entries, one for each possible outcome: (2,3,4,5...9,10,11,12). You want to keep track of how many times each of those outcomes is rolled. Start with eleven zeros [0,0,0...0,0]. Every time a 2 is rolled, the first item is has a 1 added to it. Here is a sample output, which you must include in your solution *even if you do not finish the histogram*::

     L = [30, 50, 76, 128, 129, 168, 129, 122, 83, 60]

    This list tells you that in 1,000 rolls there were 30 two's, 50 three's, 168 seven's, etc. Use a for loop to create this list, then use another for loop to draw all 11 bars in your histogram. Do not ‘hand-draw’ every bar individually. Axes should be labeled "Dice roll" and "frequency". Include coordinates for your axes as well, see the example on wamap.
   ~~~~