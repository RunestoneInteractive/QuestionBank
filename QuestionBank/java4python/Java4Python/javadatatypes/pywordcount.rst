.. activecode:: pywordcount
   :author: bmiller
   :difficulty: 3.0
   :basecourse: java4python
   :chapter: Java4Python
   :subchapter: javadatatypes
   :topics: Java4Python/javadatatypes
   :from_source: T
   :language: python

   def main():
       data = open('alice30.txt')
       wordList = data.read().split()
       count = {}
       for w in wordList:
           w = w.lower()
           count[w] = count.get(w,0) + 1

       keyList = sorted(count.keys())
       for k in keyList:
           print("%-20s occurred %4d times" % (k, count[k]))

   main()