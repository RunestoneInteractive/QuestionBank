.. mchoice:: multipleinstances_code_output
  :author: bmiller
  :difficulty: 3.0
  :basecourse: py4e-int
  :chapter: 14-objects
  :subchapter: Exercises
  :topics: 14-objects/Exercises
  :from_source: T
  :practice: T
  :answer_a: Sally
  :answer_b: Louise
  :answer_c: Sally Louise
  :answer_d: person1
  :correct: a
  :feedback_a: This prints the 'name' of the person1 instance.
  :feedback_b: 'Louise' is the 'name' of person2 but we are calling the person1 instance.
  :feedback_c: person1 and person2 are two different instances.
  :feedback_d: The output is not the name of the instace.

  What is the output of the following code?
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