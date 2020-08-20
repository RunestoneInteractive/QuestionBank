.. activecode:: db_ex3_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Debugging
   :subchapter: HowtoAvoidDebugging
   :topics: Debugging/HowtoAvoidDebugging
   :from_source: T

   current_time = input("What is the current time (in hours 0 - 23)?")
   wait_time = input("How many hours do you want to wait")

   print(current_time)
   print(wait_time)

   final_time = current_time + wait_time
   print(final_time)