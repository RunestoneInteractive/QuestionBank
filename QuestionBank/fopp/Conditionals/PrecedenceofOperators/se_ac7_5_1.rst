.. showeval:: se_ac7_5_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: PrecedenceofOperators
   :topics: Conditionals/PrecedenceofOperators
   :from_source: T
   :trace_mode: true

   5 * 3 > 10 and 4 + 6 == 11
   ~~~~
   {{5 * 3}}{{15}} > 10 and 4 + 6 == 11
   {{15 > 10}}{{True}} and 4 + 6 == 11
   True and {{4 + 6}}{{10}} == 11
   True and {{10 == 11}}{{False}}
   {{True and False}}{{False}}