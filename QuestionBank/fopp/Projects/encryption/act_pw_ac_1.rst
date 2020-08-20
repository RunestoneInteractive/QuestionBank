.. activecode:: act_pw_ac_1
    :author: bmiller
    :difficulty: 1.6325747434
    :basecourse: fopp
    :chapter: Projects
    :subchapter: encryption
    :topics: Projects/encryption
    :from_source: T
    :pct_on_first: 0.0555555556
    :total_students_attempting: 270
    :num_students_correct: 165.0
    :mean_clicks_to_correct: 11.7393939394

    implement the algorithm outlined above assuming that the user entered 'password' for their password.  Store the key in a variable called 'key'.  For testing purposes we will assume that no spaces or punctuation are included in the alphabet or the password.
    ~~~~
    password = 'password'
    # your code here
    ====
    from unittest.gui import TestCaseGui
    
    class MyTests(TestCaseGui):
    
        def testOne(self):
            self.assertEqual(key, 'paswordefghijklmnqtuvxyzbc')
    
    MyTests().main()