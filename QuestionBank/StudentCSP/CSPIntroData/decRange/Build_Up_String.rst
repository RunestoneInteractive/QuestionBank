.. activecode:: Build_Up_String
  :author: bmiller
  :difficulty: 3.0
  :basecourse: StudentCSP
  :chapter: CSPIntroData
  :subchapter: decRange
  :topics: CSPIntroData/decRange
  :from_source: T
  :tour_1: "Line by Line Tour"; 2: lst8-line1; 3: lst8-line2; 6: lst8-line3; 9: lst8-line4; 12: lst8-line5;

  # initialize the variables
  source = ["This","is","a","list"]
  slowly = []

  # loop from the last index to the first (0)
  for index in range(len(source)-1,-1,-1):

      # append the lists
      slowly = [source[index]] + slowly

      # print the current value of the list
      print(slowly)