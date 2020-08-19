.. activecode:: act_kiva_graph_4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Projects
    :subchapter: kiva_graphs
    :topics: Projects/kiva_graphs
    :from_source: T
    :pct_on_first: 0.1259259259
    :total_students_attempting: 270
    :num_students_correct: 154.0
    :mean_clicks_to_correct: 8.512987013

    Given a list of numbers compute the counts for each bucket as represented by the bucket list. (get it!)  Assume that the numbers can be in the range from 0 -- 100. Do not cheat and count these manually.  Tell yourself that test_numbers has ten thousand numbers on it.
    ~~~~
    test_numbers = [0,1,1,9,10,20,25,29,99,99,99, 74, 75, 76, 80, 89, 70, 100]
    bucket_list = [0,0,0,0,0,0,0,0,0,0]
    
    ====
    from unittest.gui import TestCaseGui
    
    class MyTests(TestCaseGui):
    
        def testOne(self):
            self.assertEqual(bucket_list[0], 4, "bucket 0")
            self.assertEqual(bucket_list[1], 1, 'bucket 1')
            self.assertEqual(bucket_list[2], 3, 'bucket 2')
            self.assertEqual(bucket_list[3], 0, 'bucket 3')
            self.assertEqual(bucket_list[4], 0, 'bucket 4')
            self.assertEqual(bucket_list[5], 0, 'bucket 5')
            self.assertEqual(bucket_list[6], 0, 'bucket 6')
            self.assertEqual(bucket_list[7], 4, 'bucket 7')
            self.assertEqual(bucket_list[8], 2, 'bucket 8')
            self.assertEqual(bucket_list[9], 4, 'bucket 9')
            self.assertTrue('for' in self.getEditorText(), "for loop check")
    
    MyTests().main()