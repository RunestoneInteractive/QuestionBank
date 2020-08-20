.. activecode:: For_Each_Range
  :author: bmiller
  :difficulty: 3.0
  :basecourse: StudentCSP
  :chapter: CSPIntroData
  :subchapter: forEach
  :topics: CSPIntroData/forEach
  :from_source: T
  :tour_1: "Line by Line Tour"; 2: lst4-line1; 3: lst4-line2; 6: lst4-line3; 7: lst4-line4;

  # initialize the variables
  myString = "MLK"
  myList = range(0,len(myString))

  # loop through the indices in myList and print each character
  for index in myList:
      print(myString[index])