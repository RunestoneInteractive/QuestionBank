.. activeCode:: Multiple_Ifs
  :author: bmiller
  :difficulty: 3.0
  :basecourse: studentcsp
  :chapter: CSPIntroDecisions
  :subchapter: practice
  :topics: CSPIntroDecisions/practice
  :from_source: T
  :tour_1: "Structural Tour"; 1: c1-line1; 2: c4-line2; 3-4: c1-line2-3; 5-6: c1-line4-5; 7: c1-line6; 8-9: c4-line8-9; 10-12: c3f-line7-9;

  weight = 0.5
  numItems = 5
  if weight < 1:
      price = 1.45
  if weight >= 1:
      price = 1.15
  total = weight * price
  if numItems >= 10:
      total = total * 0.9
  print(weight)
  print(price)
  print(total)