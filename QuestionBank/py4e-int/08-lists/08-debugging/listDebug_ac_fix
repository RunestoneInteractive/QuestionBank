.. activecode:: listDebug_ac_fix
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-debugging
    :topics: 08-lists/08-debugging
    :from_source: T
    :nocodelens:

    Fix the following code to correctly add x, y, and z to the end of lst in that order.
    ~~~~
    lst = [1, 1, 2, 3, 5, 8, 13]
    x = 21
    y = 34
    z = 55
    lst.append([x])
    lst = lst + y
    lst = lst.append(z)

    ====
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(lst,[1,1,2,3,5,8,13,21,34,55],"Testing that x, y, and z, have been added to the end of lst")

    myTests().main()