.. activecode:: writingcode_question10_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 10-tuples
   :subchapter: 10-writecode
   :topics: 10-tuples/10-writecode
   :from_source: T
   :practice: T
   :nocodelens:

   Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.
   ~~~~

   lst_tups = [('Articuno', 'Moltres', 'Zapdos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", 'Tauros', 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Seviper', 'Wailord', 'Sealeo')]

   ====
   from unittest.gui import TestCaseGui

   class MyTests(TestCaseGui):

       def testOne(self):
           self.assertEqual(t_check, ['Zapdos', 'Charizard', 'Diglett', 'Tauros', 'Lanturn', 'Seviper'], "Checking that the correct entries made it into t_check.")
           self.assertEqual(len(t_check), 6, "Making sure no entries were added or missed.")

   MyTests().main()