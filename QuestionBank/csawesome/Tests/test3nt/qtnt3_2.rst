.. mchoice:: qtnt3_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test3nt
   :topics: Tests/test3nt
   :from_source: T
   :answer_a: I only
   :answer_b: II only
   :answer_c: III only
   :answer_d: I and II only
   :answer_e: I, II, and III
   :correct: b
   :feedback_a: The color is a private instance variable in Bird. Children classes do not have direct access to private variables.  They must use the public getter and setter methods to access the private variables.
   :feedback_b: The public eat method was inherited from the Bird class and can be called from code in the Swan class.
   :feedback_c: Constructors are not inherited by sub classes. Only public accessor and mutator methods are inherited by sub classes.
   :feedback_d: II is correct, but I is incorrect. Private instance variables cannot be directly accessed by the child class.
   :feedback_e: II is correct, but I and III are incorrect. Constructors are not inherited and subclasses do not have direct access to private instance variables.
   :pct_on_first: 0.3529411765
   :total_students_attempting: 119
   :num_students_correct: 116.0
   :mean_clicks_to_correct: 2.275862069

   Consider the following class declarations. Which of the following code can be executed in the ``Swan`` class?
   
   .. code-block:: java
   
      public class Bird
      {
          private String color;
   
          public Bird(String theColor)
          {
              /* implementation not shown */
          }
   
          public void makeNoise()
          {
              /* implementation not shown */
          }
   
          public void eat()
          {
              /* implementation not shown */
          }
   
          public string showFeathers()
          {
              return color;
          }
      }
   
      public class Swan extends Bird
      {
          /* no constructors or other methods have been declared */
      }
   
   
      I. this.color = "blue";
   
      II. eat();
   
      III. Swan s = new Swan("blue");