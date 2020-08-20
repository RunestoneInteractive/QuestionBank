.. activecode:: fic
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Files
   :subchapter: With
   :topics: Files/With
   :from_source: None
   :nocodelens:

   with open('mydata.txt') as md:
       print(md)
       for line in md:
           print(line)
   print(md)