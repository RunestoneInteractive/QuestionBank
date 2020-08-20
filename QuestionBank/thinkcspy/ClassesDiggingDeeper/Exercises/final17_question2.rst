.. activecode:: final17_question2
    :author: Brad Miller
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: ClassesDiggingDeeper
    :subchapter: Exercises
    :topics: ClassesDiggingDeeper/Exercises
    :from_source: F
    :pct_on_first: 0.0588235294
    :total_students_attempting: 17
    :num_students_correct: 8.0
    :mean_clicks_to_correct: 8.125

    Given a string, write a function `first_unique(a_string)` that returns the first non-repeated character in the string.  For example if the string was "hah" your function would return a because the 'h' is repeated.  If there are no non-repeated characters then the empty string should be returned.
    ~~~~
    def first_unique(a_string):
        # your code here
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            self.assertEqual(first_unique("hello"),"h","hello")
            self.assertEqual(first_unique("stress"),"t","stress")
            self.assertEqual(first_unique("mississippi"),"m","mississippi")
            self.assertEqual(first_unique("aabbccddeeff"),"","aabbccddeeff")
            self.assertEqual(first_unique("abcdefabcdef"),"","abcdefabcdef")
            self.assertEqual(first_unique("teeter"),"r","teeter")
    
    myTests().main()