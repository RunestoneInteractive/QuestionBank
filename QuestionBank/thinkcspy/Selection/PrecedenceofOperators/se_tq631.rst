.. showeval:: se_tq631
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Selection
   :subchapter: PrecedenceofOperators
   :topics: Selection/PrecedenceofOperators
   :from_source: T
   :trace_mode: true

   5 * 3 > 10 and 4 + 6 == 11
   ~~~~
   {{5 * 3}}{{15}} > 10 and 4 + 6 == 11
   {{15 > 10}}{{True}} and 4 + 6 == 11
   True and {{4 + 6}}{{10}} == 11
   True and {{10 == 11}}{{False}}
   {{True and False}}{{False}}