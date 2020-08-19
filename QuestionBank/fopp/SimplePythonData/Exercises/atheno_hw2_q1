.. actex:: atheno_hw2_q1
   :author: Atheno Chen
   :difficulty: 3.0
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :autograde: unittest
   :pct_on_first: 0.0
   :total_students_attempting: 3
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 4.5

   Coronaviruses are a group of viruses that cause diseases in mammals and birds that include diarrhea in cows and pigs, and upper respiratory disease in chickens. In humans, the virus causes respiratory infections, which are often mild, but in rare cases, are potentially lethal. There are no vaccines or antiviral drugs that are approved for prevention or treatment. Suppose the viruses are out of control, and every single person who is infected can pass the virus to a healthy person in 24 hours. Assume the viruses start from one person. Write a program that will compute the days it needs to spread the viruses to the whole population of the country you are living in. Prompt the user to enter the population and save them to variables called ``population``. Print a sweet message back to the user with the answer. Test your program of the entire population of the earth. You can refer to the following link for the population data: https://en.wikipedia.org/wiki/World_population
   ~~~~
   # Python math module link: https://docs.python.org/3.7/library/math.html
   
   # The Python interpreter used here is a bit outdated. 
   # If you encounter any function from the above link that doesn't work here, 
   # please google/baidu it to find an alternative solution. If you could not resolve it in 10 minutes,
   # seek the help from your tutor.
   
   ====
   from unittest.gui import TestCaseGui
   class myTests(TestCaseGui):
       def test_radius(self):
           output = self.getOutput().split('\n')
           self.assertIn("population", self.getEditorText(), 'population variable')
           self.assertAlmostEqual(float(output[0]), math.ceil(math.log(int(population), 2)), 5, 'Checking answer.')
   myTests().main()