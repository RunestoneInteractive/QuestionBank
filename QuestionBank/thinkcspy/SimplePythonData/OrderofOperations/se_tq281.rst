.. showeval:: se_tq281
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: SimplePythonData
   :subchapter: OrderofOperations
   :topics: SimplePythonData/OrderofOperations
   :from_source: T
   :trace_mode: true

   16 - 2 * 5 // 3 + 1
   ~~~~
   16 - {{2 * 5}}{{10}} // 3 + 1
   16 - {{10 // 3}}{{3}} + 1
   {{16 - 3}}{{13}} + 1
   {{13 + 1}}{{14}}