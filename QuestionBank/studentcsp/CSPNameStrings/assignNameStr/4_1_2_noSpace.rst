.. mchoice:: 4_1_2_noSpace
   :author: bmiller
   :difficulty: 3.0
   :basecourse: studentcsp
   :chapter: CSPNameStrings
   :subchapter: assignNameStr
   :topics: CSPNameStrings/assignNameStr
   :from_source: T
   :practice: T
   :answer_a: 125 Main Street, Atlanta, GA
   :answer_b: 125 Main Street,Atlanta, GA
   :answer_c: 125 Main Street Atlanta, GA
   :correct: b
   :feedback_a: This would be true if it was street + ", ".
   :feedback_b: There isn't a space after the comma and one isn't added automatically.
   :feedback_c: What about the comma?

   What will be printed when the following executes?

   ::

     street = "125 Main Street"
     cityState = "Atlanta, GA"
     print(street + "," + cityState)