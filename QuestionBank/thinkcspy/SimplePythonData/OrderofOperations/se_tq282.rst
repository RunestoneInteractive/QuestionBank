.. showeval:: se_tq282
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: SimplePythonData
   :subchapter: OrderofOperations
   :topics: SimplePythonData/OrderofOperations
   :from_source: T
   :trace_mode: true

   2 ** 2 ** 3 * 3
   ~~~~
   2 ** {{2 ** 3}}{{8}} * 3
   {{2 ** 8}}{{256}} * 3
   {{256 * 3}}{{768}}