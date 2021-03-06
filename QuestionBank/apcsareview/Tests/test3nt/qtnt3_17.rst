.. mchoice:: qtnt3_17
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test3nt
   :topics: Tests/test3nt
   :from_source: T
   :answer_a: I only
   :answer_b: II only
   :answer_c: III only
   :answer_d: IV only
   :answer_e: I and IV only
   :correct: a
   :feedback_a: A SeedlessGrape IS-A fruit, so the inheritance relationship is correct. The constructor for the SeedlessGrape class has two string parameters.
   :feedback_b: The Grape class constructor has two parameters. Although a Grape IS-A fruit, the Grape constructor must have two string parameters to compile without error.
   :feedback_c: A Grape is NOT a SeedlessGrape. The inheritance relationship is incorrect, and III does not compile. Object a is a Fruit at compile-time and a SeedlessGrape at run-time. A SeedlessGrape IS-A Fruit, so the code compiles.
   :feedback_d: The Fruit class is an abstract class.  You can not create an object of an abstract class type.
   :feedback_e: I is correct, but a Fruit object cannot be instantiated. The Fruit class is an abstract class, and you can not create an object of an abstract class type.

    Consider the ``Fruit``, ``Grape``, and ``SeedlessGrape`` classes shown below. Which of the following object declarations will compile without error?

   .. code-block:: java

      public abstract class Fruit
      {
          private String name;
          private boolean seeds;

          public Fruit(String theName)
          {
              name = theName;
              seeds = true;
          }

          public void setSeeds()
          {
              seeds = !seeds;
          }

      }

      public class Grape extends Fruit
      {
          private String color;

          public Grape(String theName, String theColor)
          {
              super(theName);
              color = theColor;
          }
      }

      public class SeedlessGrape extends Grape
      {
          public SeedlessGrape(String theName, String theColor)
          {
              super(theName, theColor);
              setSeeds();
          }
      }

      I. Fruit a = new SeedlessGrape("grape", "red");
      II. Grape b = new Grape("grape");
      III. SeedlessGrape c = new Grape("grape", "green");
      IV. Fruit d = new Fruit("strawberry");