.. activecode::  str-ex-meowq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-WriteCode
    :topics: 06-strings/06-WriteCode
    :from_source: T
    :nocodelens:

    Fix the code so that only "meow" is printed.
    ~~~~
    sentence = "The cat goes meow."
    s2 = [16:13]sentence
    print(s2)

    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(s2,"meow")

    myTests().main()