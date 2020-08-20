.. activeCode:: Multiple_Ifs_2
     :author: bmiller
     :difficulty: 3.0
     :basecourse: StudentCSP
     :chapter: CSPIntroDecisions
     :subchapter: ifAndElse
     :topics: CSPIntroDecisions/ifAndElse
     :from_source: T
     :tour_1: "Structural Tour"; 1: c1-line1; 2-3: c1-line2-3; 4-5: c1-line4-5; 6: c1-line6; 7-9: c3f-line7-9;

     weight = 0.5
     if weight < 1:
         price = 1.45
     if weight >= 1:
         price = 1.15
     total = weight * price
     print(weight)
     print(price)
     print(total)