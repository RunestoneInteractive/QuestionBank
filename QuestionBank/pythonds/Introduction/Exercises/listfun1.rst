.. activecode:: listfun1
    :author: Giulia Toti
    :difficulty: 2.0
    :basecourse: pythonds
    :chapter: Introduction
    :subchapter: Exercises
    :topics: Introduction/Exercises
    :from_source: F
    :language: python
    :pct_on_first: 0.2
    :total_students_attempting: 20
    :num_students_correct: 17.0
    :mean_clicks_to_correct: 7.1764705882

    Write a function replace(list,old,new) that replaces every instance of old with new in the list.
    Note: return the list to pass the test cases. 
    ~~~~
    def replace(list,old,new):
        #Your code here
    
    test = [1,2,3,4,3]
    replace(test,3,100)
    print(test)
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            self.assertEqual(replace([1,2,3,4,3],3,100),[1,2,100,4,100],"Every 3 should be replaced with 100")
            self.assertEqual(replace(["H","e","l","l","o"], "l", "_"), ["H","e","_","_","o"], "Every l should be replaced with _")
    
    myTests().main()