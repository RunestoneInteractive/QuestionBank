.. mchoice:: partyanimal_code
  :author: bmiller
  :difficulty: 3.0
  :basecourse: py4e-int
  :chapter: 14-objects
  :subchapter: 14-ourfirstpythonobject
  :topics: 14-objects/14-ourfirstpythonobject
  :from_source: T
  :practice: T
  :answer_a: 'PartyAnimal.party(an)' creates a new object while 'an.party()' calls
              the 'party()' function within the 'an' object.
  :answer_b: Calling 'an.party()' creates a new 'PartyAnimal' instance everytime hence
             value of x is changed to 1 everytime the 'party' function is called.
  :answer_c: The word 'self' to be mentioned explicitly to make 'party' a static function.
  :answer_d: 'PartyAnimal.party(an)' and 'an.party()' are both valid ways to call the
             'party()' function within the 'an' object.
  :correct: d
  :feedback_a: The object instance is created when 'an = PartyAnimal()' is executed, the following
               statements call the 'party()' function within the instance.
  :feedback_b: 'an.party()' does not create new object instance, it calls the 'party()' function
               within the object.
  :feedback_c: 'self' is used to represent the instance of a class and to access the attributes and
               methods of the class. The only time 'self' is not mentioned explicitly is within static
               methods.
  :feedback_d: This is correct!

  What is true about the following code?

  ::

    class PartyAnimal:
      x = 0

      def party(self) :
         self.x = self.x + 1
         print("So far",self.x)

    an = PartyAnimal()
    an.party()
    an.party()
    an.party()
    PartyAnimal.party(an)