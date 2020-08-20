.. codelens:: Ketchup_Speed
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPNameNumbers
   :subchapter: ketchup
   :topics: CSPNameNumbers/ketchup
   :from_source: T

   dripMPH = .028
   FPM = 5280.0
   dripFPH = dripMPH * FPM
   MPH = 60
   dripFPM = dripFPH / MPH
   print("Ketchup speed in feet per minute:")
   print(dripFPM)
   print("Ketchup speed to move 4 feet in minutes:")
   print(4 / dripFPM)