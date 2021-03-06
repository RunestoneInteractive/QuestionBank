.. activecode:: lhs_2_2
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: SimplePythonData
    :subchapter: Exercises
    :topics: SimplePythonData/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :nocodelens: 
    :hidecode: 
    :pct_on_first: 0.2654028436
    :total_students_attempting: 422
    :num_students_correct: 400.0
    :mean_clicks_to_correct: 3.85

    How long (how many characters) is the string in the variable ``sent``? Write code to assign the length of that string to a variable called ``len_of_sent``.
    
    How long is the string in the variable ``short_sent``? Write code to assign the value of that string's length to a variable ``short_len``.
    
    Write code to print out the value of ``short_len`` (and the value of len_of_sent, if you want!) so you can see it.
    
    Consider (ungraded but important): Why is the length of ``short_sent`` longer than 15 characters?
    
    **HINT**: See 2.6 and look for a function that can return the length of a string.
    
    ~~~~
    sent = """
    He took his vorpal sword in hand:
    Long time the manxome foe he sought
    So rested he by the Tumtum tree,
    And stood awhile in thought.
    - Jabberwocky, Lewis Carroll (1832-1898)"""
    
    short_sent = """
    So much depends
    on
    """
    
    # Write your code here.
    
    
     =====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
           self.assertEqual(len_of_sent, len(sent), "Testing that len_of_sent has been set to the length of the variable sent.")
        def testTwo(self):
           self.assertEqual(short_len,len(short_sent), "Testing that short_len has been set to the length of the variable short_sent")
        def testThree(self):
           self.assertIn('20', self.getOutput(), "Testing that you printed the length of short_sent. (Don't worry about Actual and Expected Values.)")
    
    myTests().main()