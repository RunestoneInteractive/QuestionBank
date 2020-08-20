.. activecode:: Reverse_List
  :author: bmiller
  :difficulty: 3.0
  :basecourse: TeacherCSP
  :chapter: CSPIntroData
  :subchapter: revList
  :topics: CSPIntroData/revList
  :from_source: T
  :tour_1: "Line by Line Tour"; 2: lst6-line1; 5: lst6-line2; 8: lst6-line3; 11: lst6-line4; 12: lst6-line5;

  # setup the source list
  source = ["This","is","a","list"]

  # Set the accumulator to the empty list
  soFar = []

  # Loop through all the items in the source list
  for index in range(0,len(source)):

      # Add a list with the current item from source to soFar
      soFar = [source[index]] + soFar
      print(soFar)