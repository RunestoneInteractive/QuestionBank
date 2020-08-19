.. mchoice:: multipleinstances_mchoice1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 14-objects
    :subchapter: Exercises
    :topics: 14-objects/Exercises
    :from_source: T
    :practice: T
    :answer_a: person1 and person2 are two different instances of the People class.
    :answer_b: The __init__ class is used to create instances and set initial values for its attributes.
    :answer_c: As we are not updating any values, 'self' is not needed in def namePrint(self):
    :answer_d: person2 cannot access the 'name' of person1.
    :correct: c
    :feedback_a: Since two different objects were created, this is correct.
    :feedback_b: __init__ is an optional method in classes that is used to set initial values for objects.
    :feedback_c: 'self' is used to represnt the current instace of the class.
    :feedback_d: Since they are two different instaces, they cannot access each other and have different initial values too

    Which of the following statements is incorrect about the following code?
    ::

      class People():
        name = ''

        def __init__(self, name):
          self.name = name

        def namePrint(self):
          print("Name: " + self.name)

      person1 = People("Sally")
      person2 = People("Louise")
      person1.namePrint()