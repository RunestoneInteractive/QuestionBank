.. showeval:: se_mc6h
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Selection
   :subchapter: PrecedenceofOperators
   :topics: Selection/PrecedenceofOperators
   :from_source: None
   :trace_mode: true

   5 * 3 > 10 and 4 + 6 == 11
   ~~~~
   {{5 * 3}}{{15}} > 10 and 4 + 6 == 11
   {{15 > 10}}{{True}} and 4 + 6 == 11
   True and {{4 + 6}}{{10}} == 11
   True and {{10 == 11}}{{False}}
   {{True and False}}{{False}}