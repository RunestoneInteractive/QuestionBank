.. activecode:: assess_ps_01_01
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: SimplePythonData
    :subchapter: week1a2
    :topics: SimplePythonData/week1a2
    :from_source: T
    :include: assess_addl_functions
    :language: python
    :autograde: unittest

    There is a function we are providing in for you in this problem called ``square``. It takes one integer and returns the square of that integer value. Write code to assign a variable called ``xyz`` the value ``5*5`` (five squared). Use the square function, rather than just multiplying with ``*``.
    ~~~~
    xyz = ""

    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(type(xyz), type(3), "Checking type of xyz")
            self.assertEqual(xyz, 25, "Checking if xyz is 25")
            self.assertIn('square', self.getEditorText(), "Testing that 'square' is in your code. (Don't worry about Actual and Expected Values.)")

    myTests().main()