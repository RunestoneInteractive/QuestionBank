.. activecode:: writtencode_question11_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 11-regex
   :subchapter: 11-writecode
   :topics: 11-regex/11-writecode
   :from_source: T
   :available_files: mbox-short.txt

   import re

   total_emails = 0
   hand = open('mbox-short.txt5')
   for line in hand:
       line = line.rstrip()
       x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA_Z]\s?(\d)', line)
       for item in x:
           total_emails += int(item)