.. activecode:: ac14_10_6_coi_jmc
    :author: Jonny Comes
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: MoreAboutIteration
    :subchapter: ChapterAssessment
    :topics: MoreAboutIteration/ChapterAssessment
    :from_source: F
    :autograde: unittest
    :practice: T

    **Challenge:** Write a function called ``beginning`` that takes a list as input and contains a while loop that only stops once the element of the list is the string 'bye'. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If "bye" is the 5th element, the first 4 are returned.) *If you want to make this even more of a challenge, do this without slicing*
    ~~~~

    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

       def testOne(self):
          self.assertEqual(beginning(['water', 'phone', 'home', 'chapstick', 'market', 'headphones', 'bye', 'stickie notes', 'snapchat', 'facebook', 'social media']), ['water', 'phone', 'home', 'chapstick', 'market', 'headphones'], "Testing that beginning returns the correct list on input ['water', 'phone', 'home', 'chapstick', 'market', 'headphones', 'bye', 'stickie notes', 'snapchat', 'facebook', 'social media']")
          self.assertEqual(beginning(['bye', 'no', 'yes', 'maybe', 'sorta']), [], "Testing that beginning returns the correct list on input ['bye', 'no', 'yes', 'maybe', 'sorta']")
          self.assertEqual(beginning(['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning', 'sup', 'see yah', 'toodel loo', 'night', 'until later', 'peace', 'bye', 'good-bye', 'g night']),['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning', 'sup'] , "Testing that beginning returns the correct list on input ['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning', 'sup', 'see yah', 'toodel loo', 'night', 'until later', 'peace', 'bye', 'good-bye', 'g night']")

    myTests().main()