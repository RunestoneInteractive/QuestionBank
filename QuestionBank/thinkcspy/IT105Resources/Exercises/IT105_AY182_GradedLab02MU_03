.. activecode:: IT105_AY182_GradedLab02MU_03
   :author: Tom Babbitt
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: IT105Resources
   :subchapter: Exercises
   :topics: IT105Resources/Exercises
   :from_source: F
   :language: python
   :nocodelens: 
   :pct_on_first: 0.0
   :total_students_attempting: 3
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 4.0

   You are making a computer game and one of the requirements is to determine the estimated number of times an event must occur in order to have it occur between a start and end time.
   
   Write a function ``findEstimate(startTime, endTime)``
   that will take two number between 1 and 1000. The function will ``return`` an estimate for the number of time an event must occur prior to landing between the start and end time. 
   
   **Note 1:** ``1 <= startTime < endTime <= 1000`` 
   
   **Note 2:** A successful attempt occurs when a random number between 1 and 1000 falls between ``startTime`` and ``endTime``.
   
   **Note 3:** Assume for each attempt all times between 1 and 1000 are equally likely. **(If an attempt fails to fall between the times a new random number is chosen.)**
    
   Example: 
   
   ::     
      
      print(findEstimate(10,25))
       
      
   
   Results:
   
   ::
   
      ### This will be a random integer; equating to the number of attempts.
   
   
   ~~~~
   ### Name:
   
   import random
   ###write your code here.
   
   
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
      
      def golden_func(self,startTime, endTime):
         count = 1
         num = random.randint(1,1000)
         while not( startTime <= num <=endTime):
            count = count + 1
            num = random.randint(1,1000)
         return(count)
   
      def testOne(self):
         print('Auto-testing...')
         count = 0
         for i in range(1,101,5):
            a = random.randint(1,999)
            b = random.randint(a+1,1000)        	
            random.seed(i)
            answer = self.golden_func(a,b)
            random.seed(i)
            count+=1
            self.assertEqual(findEstimate(a,b), answer, "Random try # " + str(count) + "; startTime = " + str(a) + "; endTime = " + str(b))
   
   myTests().main()