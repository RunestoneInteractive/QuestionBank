.. parsonsprob:: 16_9_1_rainfall
  :author: bmiller
  :difficulty: 3.0
  :basecourse: TeacherCSP
  :chapter: CSPIntroData
  :subchapter: rainfall
  :topics: CSPIntroData/rainfall
  :from_source: T
  :numbered: left
  :adaptive:

  Construct a program that correctly solves the rainfall problem
  -----
  # initialize the variables
  rain = [0,5,1,0,-1,6,7,-2,0]
  sumRain = 0
  count = 0
  =====
  # loop through the values in the list
  for day in rain:
  =====
      # if the value of day is positive
      if day >= 0:
  =====
          # add day to the sum
          # also add one to count
          sumRain = sumRain + day
          count = count + 1.0
  =====
  # if count is positive
  if count > 0:
  =====
      # calculate and print the average
      ave = sumRain / count
      print("Average",ave)
  =====
  # otherwise
  else:
  =====
      # print no rain
      print("No rain")