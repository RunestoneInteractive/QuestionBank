.. activecode:: listfun2
    :author: Giulia Toti
    :difficulty: 2.0
    :basecourse: pythonds
    :chapter: Introduction
    :subchapter: Exercises
    :topics: Introduction/Exercises
    :from_source: F
    :language: python
    :pct_on_first: 0.6666666667
    :total_students_attempting: 18
    :num_students_correct: 18.0
    :mean_clicks_to_correct: 2.1111111111

    Write a function replace(list,old,new) that creates a new list where every instance of old is replaced with new.
    The original list must remain the same.
    ~~~~
    def replace(list,old,new):
        #Your code here
    
    test = [1,2,3,4,3]
    newlist = replace(test,3,100)
    print("Original:",test)
    print("Modified:",newlist)
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            self.assertEqual(replace([1,2,3,4,3],3,100),[1,2,100,4,100],"Every 3 should be replaced with 100")
            self.assertEqual(replace(["H","e","l","l","o"], "l", "_"), ["H","e","_","_","o"], "Every l should be replaced with _")
    
    myTests().main()