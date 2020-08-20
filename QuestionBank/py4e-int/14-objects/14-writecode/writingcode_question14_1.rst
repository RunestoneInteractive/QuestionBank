.. activecode:: writingcode_question14_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 14-objects
   :subchapter: 14-writecode
   :topics: 14-objects/14-writecode
   :from_source: T
   :nocodelens:

  class Dog:
      name = ''
      tricks = []

      def __init__(self, name):
          self.name = name

      def updateTricks(trick)
          self.tricks.append(trick)

      def __str__(self):
          return 'Dog(name = ' + self.name +  ', tricks = ' + str(self.tricks) + ')'