.. activecode:: writtencode_question11_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 11-regex
   :subchapter: 11-writecode
   :topics: 11-regex/11-writecode
   :from_source: T
   :available_files: mbox-short.txt

   import re
   hand = open('mbox-short.txt4')
   email_list = []
   for line in hand:
       line = line.rstrip()
       x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
       email_list.append(x)