.. activecode:: fileOpen3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-advancedtextparsing
   :topics: 09-dictionaries/09-advancedtextparsing
   :from_source: T
   :language: python3
   :available_files: romeo-full.txt

   import string

   with open("romeo-full.txt", "r") as filename:
       lines = filename.readlines()
       counts = {}
       for line in lines:
           for word in line.split():
               table = str.maketrans("", "", string.punctuation)
               stripped = word.translate(table)
               if stripped not in counts.keys():
                   counts[stripped] = 1
               else:
                   counts[stripped] += 1
   print(counts)