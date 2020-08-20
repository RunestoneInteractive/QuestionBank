.. activecode:: dictionariesandfiles_example_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-dictionariesandfiles
   :topics: 09-dictionaries/09-dictionariesandfiles
   :from_source: T
   :available_files: romeo.txt

   fname = input('Enter the file name: ')
   try:
       fhand = open(fname)
   except:
       print('File cannot be opened:', fname)
       exit()

   counts = dict()
   for line in fhand:
       words = line.split()
       for word in words:
           if word not in counts:
               counts[word] = 1
           else:
               counts[word] += 1

   print(counts)