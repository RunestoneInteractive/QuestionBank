.. activecode:: act_rot13_ac_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Projects
    :subchapter: encryption
    :topics: Projects/encryption
    :from_source: T
    :pct_on_first: 0.1991017964
    :total_students_attempting: 668
    :num_students_correct: 568.0
    :mean_clicks_to_correct: 6.8186619718

    Write a program that will encrypt the string referenced by the variable plaintext using the caesar cipher with a shift of 13.  Store the result in ciphertext.
    ~~~~
    plaintext = 'thequickbrownfoxjumpsoverthelazydog'
    ====
    from unittest.gui import TestCaseGui
    
    class MyTests(TestCaseGui):
    
        def testOne(self):
            self.assertTrue('ciphertext' in self.getEditorText(), "you need a ciphertext variable")
            self.assertEqual(ciphertext, 'gurdhvpxoebjasbkwhzcfbiregurynmlqbt')
    
    MyTests().main()