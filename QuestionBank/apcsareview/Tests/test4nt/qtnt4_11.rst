.. mchoice:: qtnt4_11
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test4nt
   :topics: Tests/test4nt
   :from_source: T
   :answer_a: Remove the abstract keyword from the Meal class declaration.
   :answer_b: Remove the abstract keyword from the Meal class and method declarations.
   :answer_c: Create a constructor for the Meal class.
   :answer_d: Remove the abstract keyword from the addToMenu method in the Meal class.
   :answer_e: Define the addToMenu method in the Breakfast class.
   :correct: e
   :feedback_a: Abstract methods cannot be placed in classes that are not abstract. In addition, the Meal class should remain an abstract class. Abstract classes can have many derived classes, so the Meal class can have multiple subclasses other than Breakfast.
   :feedback_b: Although this answer will allow the classes to compile, it is not the best solution. The Meal class should remain an abstract class. Abstract classes can have many derived classes, so the Meal class can have multiple subclasses other than Breakfast.
   :feedback_c: Creating a constructor for the Meal class will not make the classes compile. The problem with these classes lies in the methods, not the constructors.
   :feedback_d: In order for this to compile, the addToMenu method would also have to be defined in the Meal class - would have to have a body.
   :feedback_e: Because Meal is an abstract class and Breakfast is not, addToMenu MUST be defined in the Breakfast class. Abstract methods must be defined in the classes that implement them, if that class is not also abstract.

   Consider the ``Breakfast`` and ``Meal`` classes shown below. Currently, the ``Breakfast`` class will not compile. Which of the following is the BEST solution to make ``Meal`` and ``Breakfast`` compile and run as intended?

   .. code-block:: java

      public abstract class Meal
      {
          public abstract String getMealTime;

          public abstract List<String> getMenu();

          public abstract void addToMenu (String food);

          public abstract double getCalories();
      }

      public class Breakfast extends Meal
      {
          private double calories;
          private String time;
          private List<String> menu;

          public Breakfast (double theCalories, String theTime,
                            ArrayList<String> theMenu)
          {
              calories = theCalories;
              time = theTime;
              menu = theMenu;
          }

          public String getMealTime()
          {
             return time;
          }

          public List<String> getMenu()
          {
              return menu;
          }

          public double getCalories()
          {
               return calories;
          }
      }