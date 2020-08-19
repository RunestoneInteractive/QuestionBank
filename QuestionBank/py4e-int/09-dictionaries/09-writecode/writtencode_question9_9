.. activecode:: writtencode_question9_9
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-writecode
   :topics: 09-dictionaries/09-writecode
   :from_source: T
   :available_files: words.txt

   with open("words.txt", "r") as filename:
       word_count = {}
       lines = filename.readlines()
       for line in lines:
           for word in line.split():
               word = word.lower()
               if word not in word_count.keys():
                   word_count[word] = 0
               word_count[word] += 1
   print(word_count)