.. showeval:: se_ac2_4_1a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: FunctionCalls
   :topics: SimplePythonData/FunctionCalls
   :from_source: T
   :trace_mode: true

   Notice that we always have to resolve the expression inside the innermost parentheses first, in order to determine what input to provide when calling the functions.
   ~~~~
   print(sub({{square(3)}}{{9}}, square(1+1)))
   print(sub(9, square({{1+1}}{{2}})))
   print(sub(9, {{square(2)}}{{4}}))
   print({{sub(9, 4)}}{{5}})