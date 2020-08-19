.. activecode:: writtencode_question9_10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-writecode
   :topics: 09-dictionaries/09-writecode
   :from_source: T
   :available_files: romeo.txt

   with open("romeo3.txt", "r") as filename:
       lines = filename.readlines()
       counts = {}
       for line in lines:
           for word in line.split():
               word = word.lower()
               if word not in counts.keys():
                   counts[word] = 0
               counts[word] += 1