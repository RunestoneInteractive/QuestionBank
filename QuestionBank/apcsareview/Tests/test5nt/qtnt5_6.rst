.. mchoice:: qtnt5_6
      :author: bmiller
      :difficulty: 3.0
      :basecourse: apcsareview
      :chapter: Tests
      :subchapter: test5nt
      :topics: Tests/test5nt
      :from_source: T
      :answer_a: It is legal for the value of a static variable to be changed in a constructor.
      :answer_b: The constructor in a subclass must use the keyword super to initialize the private instance variables from its superclass.
      :answer_c: An interface never has constructors.
      :answer_d: An abstract class never has constructors.
      :answer_e: If a subclass does not explicitly provide a constructor and its superclass has just one constructor with a parameter, an error will occur when an attempt is made to create an instance of a subclass object.
      :correct: d
      :feedback_a: Static variables can still have their values changed
      :feedback_b: This is true, under the hood if you don't explicitly use the 'super' keyword, the compiler will do it for you automatically
      :feedback_c: There is no point to make your interface class have constructors because we can never make an instance of that class anyways
      :feedback_d: Can have unlimitted number of constructors
      :feedback_e: Because of the inheritance, the constructor from super class will be called and it is expecting a passed in parameter

      Which statement about constructors is ``false``?