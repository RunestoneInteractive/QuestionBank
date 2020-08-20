.. activecode:: sks_rev_6
   :author: Shishir Shah
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F

   The program below counts occurrences of letters in the file. 
   For example, if the input file has only this content: “Quiz 2” then the program should print 4 as a result, 
   since only 4 letters appear in the file. However, the file doesn’t work. 

   Fix any syntax and/or logical bugs so that the program executes correctly.

   ::

     def countAlpha():
           letters = 0
           for c in text:
                if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                   letters += 1

     inputFile = open('test.txt', 'w')
     fileContent = inputFile.read()
     print(fileContent)

     print(countAlpha(fileContent))


   ~~~~
   # Write the error free program here