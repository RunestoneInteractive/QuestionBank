.. activecode:: ICE_LSN08_03
   :author: jenkins
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: ICE
   :subchapter: ICE_LSN08_01
   :topics: ICE/ICE_LSN08_01
   :from_source: F
   :nocodelens:

   import random                                           # 1. import modules
   import datetime

   def bubbleSort(alist):
      for passnum in range(len(alist)-1,0,-1):
         for i in range(passnum):
            if alist[i]>alist[i+1]:
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp


   my_randoms = random.sample(range(1000),1000)          # 2. Creates a list of random numbers
   my_randoms2 = list(my_randoms)                        # 3. Creates a copy of the random list

   a = datetime.datetime.now()                           # 4. Start time for sort()
   my_randoms.sort()                                     # 5. Sort the list using sort()
   b = datetime.datetime.now()                           # 6. End time for sort()
   print(b-a)                                            # 7. Print the difference

   # your code goes here