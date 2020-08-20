.. activecode:: splitCityState2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPWebData
   :subchapter: findPollState
   :topics: CSPWebData/findPollState
   :from_source: T
   :tour_1: "Line-by-line tour"; 1: state2-line1; 2: state2-line2; 3: state2-line3; 4: state2-line4; 5: state2-line5; 6: state2-line6; 7: state2-line7;

   line = "Yuba City, CA :12 :7"
   pieces = line.split(":")
   print("All the pieces:")
   print(pieces)
   cityState = pieces[0].split(",")
   print("City:", cityState[0])
   print("State:", cityState[1])