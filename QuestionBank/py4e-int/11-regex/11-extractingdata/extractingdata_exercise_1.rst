.. activecode:: extractingdata_exercise_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 11-regex
   :subchapter: 11-extractingdata
   :topics: 11-regex/11-extractingdata
   :from_source: T
   :nocodelens:

   import re
   s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
   lst = re.findall('\S+@\S+', s)
   print(lst)