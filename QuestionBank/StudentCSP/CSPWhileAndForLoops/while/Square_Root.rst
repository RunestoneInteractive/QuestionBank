.. activecode:: Square_Root
  :author: bmiller
  :difficulty: 3.0
  :basecourse: StudentCSP
  :chapter: CSPWhileAndForLoops
  :subchapter: while
  :topics: CSPWhileAndForLoops/while
  :from_source: T
  :tour_1: "Line by line tour"; 1: sqR_line1; 2: sqR_line2; 3: sqR_line3; 4: sqR_line4; 5: sqR_line5; 6: sqR_line6; 7: sqR_line7; 8: sqR_line8;

  target = 6
  guess = 2
  guessSquared = guess * guess
  while abs(target-guessSquared) > 0.01:
      closer = target / guess
      guess = (guess + closer) / 2.0
      guessSquared = guess * guess
  print("Square root of", target,"is", guess)