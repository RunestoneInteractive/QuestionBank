.. parsonsprob:: question9_3_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-dictionariesandfiles
   :topics: 09-dictionaries/09-dictionariesandfiles
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:

   Construct a block of code to read through the lines of a file, break each line into a list of words, and then loop through each of the words in the line and count each word using a dictionary.
   -----
   file_to_read = "textfile.txt"
   =====
   with open(file_to_read, "r") as filename:
   =====
   with open(file_to_read, "w") as filename: #distractor
   =====
    lines = filename.readlines()
   =====
    word_count = {}
   =====
    word_count = dictionary() #distractor
   =====
    for line in lines:
   =====
    for word in lines.split() #distractor
   =====
     for word in lines.split():
   =====
      if word not in word_count.keys():
   =====
       word_count[word] = 0
   =====
      counts[word] += 1
   =====
   print(word_count)