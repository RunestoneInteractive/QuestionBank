.. activecode::  ch17ex19a
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPStringPieces
    :subchapter: ch17_exercises
    :topics: CSPStringPieces/ch17_exercises
    :from_source: T
    :nocodelens:

    def tellAnimalStory(name, gender, animal, animalName, description):

        if (gender.find("female") > -1):
            line1 = "Once upon a time there was a girl named, " + name + "."
            line2 = "She had a " + description + " " + animal + " named " + animalName + "."
        else:
            line1 = "Once upon a time there was a boy name, " + name + "."
            line2 = "He had a " + description + " " + animal + " named " + animalName + "."

        print(line1)
        print(line2)

    tellAnimalStory("Barb", "female", "horse","Sport","handsome")
    tellAnimalStory("Mark", "male", "dog","Baxter","funny")