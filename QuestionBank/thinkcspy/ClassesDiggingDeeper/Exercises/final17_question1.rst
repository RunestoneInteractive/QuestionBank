.. activecode:: final17_question1
    :author: Brad Miller
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: ClassesDiggingDeeper
    :subchapter: Exercises
    :topics: ClassesDiggingDeeper/Exercises
    :from_source: F
    :pct_on_first: 0.0
    :total_students_attempting: 17
    :num_students_correct: 4.0
    :mean_clicks_to_correct: 15.5

    Given a list of numbers, write a function that returns the 2 largest numbers in the list.  Your program should return a list of the two numbers with the smaller of the two first and the largest second. If there are not two distinct numbers in the original list then your function should return a list of one number.  Your function may not modify the original list.
    ~~~~
    def find_two_largest(num_list):
        # Your code here
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            startlist = [24, 22, 23, 23, 25]
            self.assertEqual(find_two_largest([1,2,3,4,5,6]),[5, 6],"input: [1, 2, 3, 4, 5, 6]")
            self.assertEqual(find_two_largest([17, 15, 13, 11, 9]),[15, 17],"input: [17, 15, 13, 11, 9]")
            self.assertEqual(find_two_largest(startlist),[24, 25],"input: [24, 22, 23, 23, 25]")
            self.assertEqual(startlist, [24, 22, 23, 23, 25], "You may not change the list.")
            self.assertEqual(find_two_largest([29, 27, 26, 25, 28]),[28, 29],"input: [29, 27, 26, 25, 28]")
            self.assertEqual(find_two_largest([1, 2]),[1, 2],"input: [1, 2]")
            self.assertEqual(find_two_largest([]),[],"input: []")
            self.assertEqual(find_two_largest([99]),[99],"input: [99]")
            self.assertEqual(find_two_largest([44, 45, 45, 45, 45, 41, 42]), [44,45],"input: [44, 45, 45, 45, 45, 41, 42]")
            self.assertEqual(find_two_largest([5,5,5,5,5]),[5],"input: [5,5,5,5,5]")
    
    myTests().main()