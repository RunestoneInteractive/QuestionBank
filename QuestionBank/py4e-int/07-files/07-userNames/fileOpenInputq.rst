.. activecode:: fileOpenInputq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-userNames
    :topics: 07-files/07-userNames
    :from_source: T
    :practice: T

    fname = input('Enter the file name: '
    fhand = open(file)
    count = 1
    for line in fhand:
        if line.endswith('Received:'):
        count = count + 1
    print('There were', count, 'lines starting with "Received:" in the file', fname)

    =====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(count,243,"Remember to start counting from zero")

    myTests().main()