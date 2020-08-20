.. activecode:: ClassTestOneNoTest
    :author: Wesley Thang
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: ClassesBasics
    :subchapter: Exercises
    :topics: ClassesBasics/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 3.0

    Create a class called ``Apple`` that contains one instance variable, quantity.
    Write a class method called ``increase`` that increases the quantity by 1
    each time it is run. Assign to the variable tester, an instance of ``Apple``
    that has an initial quantity of 4. Assign to the variable ``initial_quantity``
    the value of tester's quantity without hardcoding. Call the method four times. 
    
    ~~~~
    #Define the class here
    
    
    #Your test code here
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            SelfTest = True
            if (SelfTest):
                self.assertEqual(0,1,"Auto-testing if OFF - you must check the program yourself for now")
                return
    
        def testOne(self):
            self.assertEqual(tester.quantity, 8, "Testing that testOne has the correct value assigned.")
        def testTwo(self):   
            self.assertEqual(initial_quantity, 4, "Testing that initial_quantity has the correct value assigned.")
    
         
    myTests().main()