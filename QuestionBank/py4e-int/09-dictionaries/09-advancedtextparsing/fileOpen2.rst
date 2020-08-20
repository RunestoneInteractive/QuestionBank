.. activecode:: fileOpen2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-advancedtextparsing
   :topics: 09-dictionaries/09-advancedtextparsing
   :from_source: T
   :available_files: romeo.txt

   with open("romeo2.txt", "r") as filename:
       lines = filename.readlines()
       counts = {}
       for line in lines:
           for word in line.split():
               if word not in counts.keys():
                   counts[word] = 1
               else:
                   counts[word] += 1
   print(counts)