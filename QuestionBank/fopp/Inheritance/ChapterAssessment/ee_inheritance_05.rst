.. activecode:: ee_inheritance_05
   :author: bmiller
   :difficulty: 1.1459170013
   :basecourse: fopp
   :chapter: Inheritance
   :subchapter: ChapterAssessment
   :topics: Inheritance/ChapterAssessment
   :from_source: T
   :tags: Inheritance/inheritVarsAndMethods.rst
   :pct_on_first: 0.2105263158
   :total_students_attempting: 133
   :num_students_correct: 88.0
   :mean_clicks_to_correct: 3.4772727273

   Along with the ``Pokemon`` parent class, we have also provided several subclasses. Write another method in the parent class that will be inherited by the subclasses. Call it ``opponent``. It should return which type of pokemon the current type is weak and strong against, as a tuple.
   
   - **Grass** is weak against *Fire* and strong against *Water*
   - **Ghost** is weak against *Dark* and strong against *Psychic*
   - **Fire** is weak against *Water* and strong against *Grass*
   - **Flying** is weak against *Electric* and strong against *Fighting*
   
   For example, if the ``p_type`` of the subclass is ``'Grass'``, ``.opponent()`` should return the tuple ``('Fire', 'Water')``
   ~~~~
   class Pokemon():
       attack = 12
       defense = 10
       health = 15
       p_type = "Normal"
   
       def __init__(self, name,level = 5):
           self.name = name
           self.level = level
           self.weak = "Normal"
           self.strong = "Normal"
   
       def train(self):
           self.update()
           self.attack_up()
           self.defense_up()
           self.health_up()
           self.level = self.level + 1
           if self.level%self.evolve == 0:
               return self.level, "Evolved!"
           else:
               return self.level
   
       def attack_up(self):
           self.attack = self.attack + self.attack_boost
           return self.attack
   
       def defense_up(self):
           self.defense = self.defense + self.defense_boost
           return self.defense
   
       def health_up(self):
           self.health = self.health + self.health_boost
           return self.health
   
       def update(self):
           self.health_boost = 5
           self.attack_boost = 3
           self.defense_boost = 2
           self.evolve = 10
   
       def __str__(self):
           self.update()
           return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)
   
   class Grass_Pokemon(Pokemon):
       attack = 15
       defense = 14
       health = 12
       p_type = "Grass"
   
       def update(self):
           self.health_boost = 6
           self.attack_boost = 2
           self.defense_boost = 3
           self.evolve = 12
   
   class Ghost_Pokemon(Pokemon):
       p_type = "Ghost"
   
       def update(self):
           self.health_boost = 3
           self.attack_boost = 4
           self.defense_boost = 3
   
   class Fire_Pokemon(Pokemon):
       p_type = "Fire"
   
   class Flying_Pokemon(Pokemon):
       p_type = "Flying"
   
   =====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
      def testOneA(self):
         self.assertEqual(Grass_Pokemon("Buggy").opponent(), ("Fire", "Water"), "Testing that Grass weak and strong are assigned to correct values.")
      def testOneB(self):
         self.assertEqual(Fire_Pokemon("Buggy").opponent(), ("Water", "Grass"), "Testing that Fire weak and strong are assigned to correct values.")
      def testOneC(self):
         self.assertEqual(Ghost_Pokemon("Buggy").opponent(), ("Dark", "Psychic"), "Testing that Ghost weak and strong are assigned to correct values.")
      def testOneD(self):
         self.assertEqual(Flying_Pokemon("Buggy").opponent(), ("Electric", "Fighting"), "Testing that Flying weak and strong are assigned to correct values.")
   
   myTests().main()