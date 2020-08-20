.. parsonsprob:: mixedupcode_question10_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 10-tuples
   :subchapter: 10-mixedupcode
   :topics: 10-tuples/10-mixedupcode
   :from_source: T
   :numbered: left
   :adaptive:

   Construct a block of code that uses tuples to keep track of the word count in the file 'heineken.txt'. Then print out the 10 most occuring words from the file.
   -----
   with open("heineken.txt", "r") as filename:
   =====
    lines = filename.readlines()
   =====
    word_counter = {}
   =====
    for line in lines.split():
   =====
    for line in line.split(): #distractor
   =====
     for word in line:
   =====
      if word not in word_counter.keys():
   =====
       word_counter[word] = 0
   =====
      word_counter[word] += 1
   =====
    list_of_tuples = list(word_counter.items) #distractor
   =====
    list_of_tuples = list(word_counter.items())
   =====
    list_of_tuples.sort(key = lambda x: (x[1], x[0][0]), reverse = True)
   =====
    print(list_of_tuples[:10])