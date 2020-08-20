.. activecode:: wvu_sequences_aliases
   :author: Brian Powell
   :difficulty: 1.1665731024
   :basecourse: fopp
   :chapter: TransformingSequences
   :subchapter: Exercises
   :topics: TransformingSequences/Exercises
   :from_source: F
   :autograde: unittest
   :pct_on_first: 0.2649006623
   :total_students_attempting: 151
   :num_students_correct: 93.0
   :mean_clicks_to_correct: 3.8279569892

   Create an alias named **cities** that points to the same list as the existing **municipalities** variable. Then, create a list named **towns** that is a clone of **cities**. **towns** and **cities** should be independent objects and not aliases.
   
   Once you have created the lists, change "Blacksville" in **municipalities** to "Town of Blacksville". Print out the content of element 4 in each list.
   ~~~~
   municipalities = ['Morgantown', 'Star City', 'Westover', 'Granville', 'Blacksville']
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
      def testOne(self):
        self.assertEqual(id(cities),id(municipalities),"cities and municipalities must point to the same list")
   
      def testTwo(self):
        self.assertNotEqual(id(cities),id(towns),"cities and towns must not point to the same list")
        self.assertEqual(cities[0],towns[0],"cities and towns should have the same municipalities listed")
   
      def testThree(self):
        self.assertEqual(municipalities[4],"Town of Blacksville","Blacksville should be changed to Town of Blacksville")
   
   myTests().main()