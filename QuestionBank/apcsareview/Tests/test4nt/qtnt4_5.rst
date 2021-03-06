.. mchoice:: qtnt4_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test4nt
   :topics: Tests/test4nt
   :from_source: T
   :answer_a: I only
   :answer_b: II only
   :answer_c: III only
   :answer_d: I and II only
   :answer_e: II and III only
   :correct: e
   :feedback_a: Color is a private instance variable located in the Animal class. Private instance variables cannot be directly accessed using dot notation in external classes.
   :feedback_b: getWeight and makeNoise are abstract methods in the Animal class, so they can both be used by anything declared to be of the type Animal.
   :feedback_c: getWeight and makeNoise are abstract methods in the Animal class, so they can both be used by anything declared to be of the type Animal.
   :feedback_d: Color is a private instance variable located in the Animal class. Private instance variables cannot be directly accessed using dot notation in external classes.
   :feedback_e: getWeight and makeNoise are both defined in the Animal class, so they can both be used by anything declare to be of the type Animal.

   Consider the ``Animal`` and ``Cat`` classes, shown below. In another class, the line ``Animal fluffy = new Cat ("orange", "Fluffy", 11)`` appears. Which of the following declarations will compile without error?

   .. code-block:: java

      public abstract class Animal
      {
          private String color;
          private String name;

          public Animal (String theColor, String theName)
          {
              name = theName;
              color = theColor;
          }

          public abstract String makeNoise();

          public abstract int getWeight();
      }

      public class Cat extends Animal
      {
          private int weight;

          public Cat (String theColor, String theName, int theWeight)
          {
              super (theColor, theName);
              weight = theWeight;
          }

          public String makeNoise()
          {
              return "Meow!";
          }

          public int getWeight()
          {
              return weight;
          }
      }

      I. fluffy.color;

      II. fluffy.getWeight();

      III. fluffy.makeNoise();