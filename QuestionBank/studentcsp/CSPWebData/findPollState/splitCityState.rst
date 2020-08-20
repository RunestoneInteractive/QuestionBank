.. activecode:: splitCityState
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPWebData
   :subchapter: findPollState
   :topics: CSPWebData/findPollState
   :from_source: T
   :tour_1: "Line-by-line tour"; 1: state1-line1; 2: state1-line2; 3: state1-line3; 4: state1-line4; 5: state1-line5; 6: state1-line6; 7: state1-line7;

   line = "Yuma, AZ :14 :9"
   pieces = line.split(":")
   print("All the pieces:")
   print(pieces)
   cityState = pieces[0].split(" ")
   print("City:", cityState[0])
   print("State:", cityState[1])
   print("PM 10:", pieces[1])
   print("PM 2.5:", pieces[2])