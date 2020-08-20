.. activecode:: assess_ps_02_02
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Iteration
    :subchapter: week2a2
    :topics: Iteration/week2a2
    :from_source: T
    :language: python
    :autograde: unittest
    :practice: T
    :topics: Iteration/Listsandforloops

    Write one for loop to print out each element of the list ``several_things``. Then, write *another* for loop to print out the TYPE of each element of the list ``several_things``. To complete this problem you should have written two different for loops, each of which iterates over the list ``several_things``, but each of those 2 for loops should have a different result.
    ~~~~
    several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

      def test_output(self):
          self.assertIn('for', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")
          str1 = "hello\n2\n4\n6.0\n7.5\n234352354\nthe end\n\n99\n<class 'str'>\n<class 'int'>\n<class 'int'>\n<class 'float'>\n<class 'float'>\n<class 'int'>\n<class 'str'>\n<class 'str'>\n<class 'int'>"
          str2 = "hello\n2\n4\n6.0\n7.5\n234352354\nthe end\n\n99\n<type 'str'>\n<type 'int'>\n<type 'int'>\n<type 'float'>\n<type 'float'>\n<type 'int'>\n<type 'str'>\n<type 'str'>\n<type 'int'>"
          self.assertTrue(str1 in self.getOutput() or str2 in self.getOutput(), "Testing output (Don't worry about actual and expected values).")

    myTests().main()