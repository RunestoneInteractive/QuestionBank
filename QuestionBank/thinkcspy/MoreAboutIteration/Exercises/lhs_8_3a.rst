.. activecode:: lhs_8_3a
    :author: LHS CS Team
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: Exercises
    :topics: MoreAboutIteration/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :nocodelens: 
    :pct_on_first: 0.6
    :total_students_attempting: 45
    :num_students_correct: 33.0
    :mean_clicks_to_correct: 1.5757575758

    Each time Kevin re-reads his Python book (which happens every month), he learns 10%
    of whatever material he didn’t know before. He needs to score at least 95% on his
    final exam to get an A in the class. When Kevin started, he knew nothing about Python.
    Write a function ``getLearningTime(rate, target)`` that simulates Kevin’s learning
    progress and returns the number of months it will take him to get ready for the exam.
    
    ~~~~
    def getLearningTime(rate, target):
        # your code here
        
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def _getLearningTime(self, rate, target):
            months = 0
            total = 0.0
            while total < target:
                total += (1 - total) * rate
                months += 1
            return months
    
        def testOne(self):
            r = 0.10
            t = 0.95
            mExpected = self._getLearningTime(r, t)
            mActual = getLearningTime(r, t)
            self.assertEqual(mActual, mExpected, "checking return for getLearningTime(" + str(r) + ", " + str(t))
            r = 0.20
            t = 0.90
            mExpected = self._getLearningTime(r, t)
            mActual = getLearningTime(r, t)
            self.assertEqual(mActual, mExpected, "checking return for getLearningTime(" + str(r) + ", " + str(t))
    
    myTests().main()