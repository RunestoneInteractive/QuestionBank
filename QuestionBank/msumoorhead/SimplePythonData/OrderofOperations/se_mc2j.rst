.. showeval:: se_mc2j
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: SimplePythonData
   :subchapter: OrderofOperations
   :topics: SimplePythonData/OrderofOperations
   :from_source: None
   :trace_mode: true

   16 - 2 * 5 // 3 + 1
   ~~~~
   16 - {{2 * 5}}{{10}} // 3 + 1
   16 - {{10 // 3}}{{3}} + 1
   {{16 - 3}}{{13}} + 1
   {{13 + 1}}{{14}}