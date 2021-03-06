.. activecode:: LHSChapterSixteenQuestionTwelve
    :author: Wesley Thang
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: ClassesBasics
    :subchapter: Exercises
    :topics: ClassesBasics/Exercises
    :from_source: F
    :language: python
    :autograde: unittest

    This problem will modify your previously defined class, ``bank``. Add two more methods,
    ``add_deposit`` and ``less_withdrawals``. The ``add_deposit`` method should add
    the deposit amount to ``amt`` and the ``less_withdrawals`` method should subtract
    the withdrawal amount from ``amt``. Create two instances of the class, the first
    assigned to ``bob`` and the second to ``sally``. The first uses "Bob" as the name,
    100 as the initial amount, and 50 as the deposit amount. The second uses "Sally" as the name,
    200 as the initial amount and 125 as the withdrawal amount.
    For ``bob``, call ``add_deposit`` enough times so that the bank account is 200 dollars and
    save to the variable ``bob_amt``. For ``sally``, call ``less_withdrawal`` enough times
    so that the bank account is 75 dollars and save to the variable ``sally_amt``.

    ~~~~
    #Define the class here

    #Your test code here
    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):
        def testOne(self):
            SelfTest = False
            if (SelfTest):
                self.assertEqual(0,1,"Auto-testing if OFF - you must check the program yourself for now")
                return

        def testFourA(self):
            self.assertEqual(bob.__str__(), "Your account, Bob, has 200 dollars.", "Testing that bob is assigned to correct value")
        def testFourB(self):
            self.assertEqual(sally.__str__(), 'Your account, Sally, has 75 dollars.', "Testing that sally is assigned to correct value")
        def testFourC(self):
            self.assertEqual(bob_amt, 200, "Testing that bob_amt is assigned to correct value")
        def testFourD(self):
            self.assertEqual(sally_amt, 75, "Testing that sally is assigned to correct value")
        
    myTests().main()