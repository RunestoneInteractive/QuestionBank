.. activecode:: wvu_finalexam_readcontents
    :author: Brian Powell
    :difficulty: 1.2871485944
    :basecourse: fopp
    :chapter: Files
    :subchapter: Exercises
    :topics: Files/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.0727272727
    :total_students_attempting: 55
    :num_students_correct: 16.0
    :mean_clicks_to_correct: 5.875

    Write code to open the file **so_survey.csv** and read its contents into a list named **survey_results**. Each entry in the list should correspond with one line from the original file. Ensure the file is closed when you are done reading from it.
    
    Strip whitespace from each element in **survey_results**, then split the contents of each element by the ``|`` symbol. Construct a new list named **split_results** that contains the results of the splits.
    ~~~~
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            test_one = "open(" in self.getEditorText()
            self.assertEqual(test_one, True, "File opened.")
    
            test_two = "with" in self.getEditorText() or "close()" in self.getEditorText()
            self.assertEqual(test_two, True, "File closed.")
    
            with open('so_survey.csv') as test_data_file:
                test_survey_results = test_data_file.readlines()
            self.assertEqual(survey_results, test_survey_results, "Input read in correctly.")
    
            test_four = "strip()" in self.getEditorText()
            self.assertEqual(test_four, True, "Whitespace stripped.")
    
            test_five = "split('|')" in self.getEditorText() or 'split("|")' in self.getEditorText()
            self.assertEqual(test_five, True, "Split file contents.")
    
            test_split_results = [line.strip().split('|') for line in test_survey_results]
            self.assertEqual(split_results, test_split_results, "Results are split and stripped of whitespace.")
    
    
    myTests().main()