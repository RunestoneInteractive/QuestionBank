.. activecode:: wvu_exceptions_filenotfound
    :author: Brian Powell
    :difficulty: 1.0634332201
    :basecourse: fopp
    :chapter: Exceptions
    :subchapter: Exercises
    :topics: Exceptions/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.3571428571
    :total_students_attempting: 14
    :num_students_correct: 13.0
    :mean_clicks_to_correct: 2.0769230769

    The **read_file()** function below opens the specified filename and returns a list containing each line of its contents.
    
    Modify the code so that if the specified filename doesn't exist, a "File not found" message is printed and an empty list is returned. Any other type of exception should result in your program stopping.
    
    You will need to catch **IOError** exceptions as Runestone doesn't support the more specific **FileNotFoundError** type.
    ~~~~
    def read_file(filename):
        with open(filename) as file:
            lines = file.readlines()
        return lines
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertEqual(len(read_file('so_survey.csv')),2001,"Code works fine when file exists")
            self.assertEqual(len(read_file('file_not_found.csv')),0,"Empty list returned when file does not exist")
    
    myTests().main()