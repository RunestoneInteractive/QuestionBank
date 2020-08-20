.. mchoice:: object_oriented_output
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 14-objects
    :subchapter: Exercises
    :topics: 14-objects/Exercises
    :from_source: T
    :practice: T
    :answer_a: Grass type pokemon name is Bulbasaur
               Pokemon name is Charizard and type is Fire
    :answer_b: Pokemon name is Bulbasaur and type is Grass
               Pokemon name is Charizard and type is Fire
    :answer_c: Grass type pokemon name is Bulbasaur
               Grass type pokemon name is Charizard
    :answer_d: Error because the extending class has a stringPokemon() function
               which already exists.
    :correct: a
    :feedback_a: A child class can inherit functions from parent class and also override them.
    :feedback_b: The stringPokemon() functions is changed inside the GrassType class.
    :feedback_c: The stringPokemon() functions is only changed for GrassType class but remains unchanged
                 in the original class.
    :feedback_d:  A class inherits functions from another class and override them in any way. Only the
                  construtor class cannot be changed.

    What is the output of the following code?

    ::

      class Pokemon():
        name = ''
        type = ''

        def __init__(self, name, type):
            self.name = name
            self.type = type

        def stringPokemon(self):
            print("Pokemon name is {} and type is {}".format(self.name, self.type))

      class GrassType(Pokemon):

        # overrides the stringPokemon() function on 'Pokemon' class
        def stringPokemon(self):
            print("Grass type pokemon name is {}".format(self.name))

     poke1 = GrassType('Bulbasaur', 'Grass')
     poke1.stringPokemon
     poke1.stringPokemon()
     poke2 = Pokemon('Charizard', 'Fire')
     poke2.stringPokemon
     poke2.stringPokemon()