.. activecode:: dbc
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Debugging
   :subchapter: HowtoAvoidDebugging
   :topics: Debugging/HowtoAvoidDebugging
   :from_source: None

   current_time_str = input("What is the current time (in hours 0-23)?")
   wait_time_str = input("How many hours do you want to wait?")

   current_time_int = int(current_time_str)
   wait_time_int = int(wait_time_str)

   final_time_int = current_time_int + wait_time_int
   print(final_time_int)
   #