.. activecode:: final17_question3
    :author: Brad Miller
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: ClassesDiggingDeeper
    :subchapter: Exercises
    :topics: ClassesDiggingDeeper/Exercises
    :from_source: F
    :pct_on_first: 0.0625
    :total_students_attempting: 16
    :num_students_correct: 6.0
    :mean_clicks_to_correct: 8.0

    An anagram is a word that is spelled with the exact same letters as another word (but in a different order)  Spaces in either word should be ignored as should capitalization. Write a function `is_anagram(w1,w2)` that accepts two strings as parameters.  Your function should return `True` if the two words are anagrams and `False` if they are not.
    ~~~~
    def is_anagram(w1, w2):
        # your code here
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            self.assertTrue(is_anagram("aa","aa"),"Tested input was aa and aa")
            self.assertTrue(is_anagram("luther","hurtle"),"Tested input was luther and hurtle")
            self.assertFalse(is_anagram("luther","hurtles"),"Tested input was luther and hurtles")
            self.assertFalse(is_anagram("luthers","hurtle"),"Tested input was luthers and hurtle")
            self.assertFalse(is_anagram("are","area"),"Tested input was are and area")
            self.assertFalse(is_anagram("ban","banana"), "tested input was ban and banana")
            self.assertFalse(is_anagram("","hurtle"),"Tested input was '' and hurtle")
            self.assertFalse(is_anagram("luther",""),"Tested input was luther and ''")
            self.assertTrue(is_anagram("american","macerain"),"Tested on american and macerain")
            self.assertTrue(is_anagram("american","macerain"),"Tested on american and MacEraIn")
            self.assertTrue(is_anagram("American","Mac Era In"),"Tested on American and Mac Era In")
    
    myTests().main()