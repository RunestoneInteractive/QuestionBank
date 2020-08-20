.. activecode:: writingcode_question14_2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: py4e-int
  :chapter: 14-objects
  :subchapter: 14-writecode
  :topics: 14-objects/14-writecode
  :from_source: T
  :nocodelens:

  class Pokemon:
    name = ''
    type = ''

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def stringPokemon(self):
        print("Pokemon name is {} and type is {}".format(self.name, self.type))
        print("Attacks include: " + str(self.attacks))

 bulbasaur = Pokemon('Bulbasaur', 'Grass')
 bulbasaur.updateAttacks('Vine Whip')
 bulbasaur.updateAttacks('Tackle')