.. datafile:: class1Data.txt
   :author: Tom Babbitt
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Files
   :subchapter: Exercises
   :topics: Files/Exercises
   :from_source: F

   tom 90 95 91 72
   chip 91 94 90 74
   kyle 92 92 94 86

.. datafile:: class2Data.txt
   
   tim 92 95 91 72 67
   bob 93 94 90 78 77 90
   steve 92 92 94 70 52
   
.. datafile:: class3Data.txt
   
   matt 89 94 90 72 88
   angie 98 94 90 87 77 91
   sarah 98 92 94 78 85

.. activecode:: IT105_AY182_ProblemSet03_05
   :language: python
   :nocodelens:
   :available_files: class1Data.txt, class2Data.txt, class3Data.txt

   Write a function ``findTopStudent(file)`` that will take a class file and 
   ``return`` the student's name with the best average. 

   class1Data.txt

   ::

      tom 90 95 91 72
      chip 91 94 90 74
      kyle 92 92 94 86
   
   Example:

   ::     
      
      ### myFile is a properly openned using ``class1Data.txt``
      findTopStudent(myFile) 
      
   
   Results:

   ::     
      
      kyle 

   ~~~~
   ### Name:

   ### define the findTopStudent(file) function here

   ### write any test case to test your function
   
   
   ====
   print("Check your results against the picture.")