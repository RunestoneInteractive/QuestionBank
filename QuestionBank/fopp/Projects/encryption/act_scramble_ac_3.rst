.. activecode:: act_scramble_ac_3
    :author: bmiller
    :difficulty: 1.2111694642
    :basecourse: fopp
    :chapter: Projects
    :subchapter: encryption
    :topics: Projects/encryption
    :from_source: T
    :pct_on_first: 0.3879472693
    :total_students_attempting: 531
    :num_students_correct: 429.0
    :mean_clicks_to_correct: 4.5850815851

    Write a program that will encrypt the plaintext.  Store your encrypted message in the variable ciphertext.
    ~~~~
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    key = 'mwgp bdzxrylacsokjfhtnueivq'
    plaintext = 'of shoes and ships and sealing wax of cabbages and kings'
    ====
    from unittest.gui import TestCaseGui
    
    class MyTests(TestCaseGui):
    
        def testOne(self):
            self.assertEqual(ciphertext, 'sbqfzs fqmcpqfzxofqmcpqf mlxcdqumeqsbqgmwwmd fqmcpqyxcdf')
    
    MyTests().main()