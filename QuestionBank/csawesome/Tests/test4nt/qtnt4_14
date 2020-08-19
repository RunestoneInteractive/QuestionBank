.. mchoice:: qtnt4_14
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Tests
   :subchapter: test4nt
   :topics: Tests/test4nt
   :from_source: T
   :answer_a: II only
   :answer_b: IV only
   :answer_c: I and II only
   :answer_d: I and IV only
   :answer_e: II and III only
   :correct: e
   :feedback_a: getColor and numOfWheels are both public methods of the Vehicle class and so the code will compile.
   :feedback_b: color is a private instance variable located in the Vehicle class. Private instance variables can not be directly accessed using dot notation in external classes.
   :feedback_c: wheels is a private instance variable located in the Vehicle class. Private instance variables can not be directly accessed using dot notation in external classes.
   :feedback_d: wheels and color are both private instance variables in the Vehicle class. Private instance variables can not be directly accessed using dot notation in external classes.
   :feedback_e: getColor and numOfWheels are both public methods in the Vehicle class and can be invoked in any class on a variable of type Vehicle.
   :pct_on_first: 0.6063829787
   :total_students_attempting: 94
   :num_students_correct: 91.0
   :mean_clicks_to_correct: 1.8131868132

   The ``Vehicle``, ``Bike``, and ``Car`` classes are shown. The objects ``a`` and ``b`` have been declared in a different class. Which of the following lines will compile without error?
   
   .. code-block:: java
   
       public class Vehicle
       {
           private int wheels;
           private String color;
   
           public Vehicle (String theColor, int theWheels)
           {
               wheels = theWheels;
               color = theColor;
           }
   
           public int numOfWheels()
           {
               return wheels;
           }
   
           public String getColor()
           {
               return color;
           }
       }
   
       public class Bike extends Vehicle
       {
           public Bike (String theColor, int theWheels)
           {
               super (theColor, theWheels);
           }
   
           /* no other constructors or methods implemented */
       }
   
       public class Car extends Vehicle
       {
           public Car (String theColor, int theWheels()
           {
               super (theColor, theWheels);
           }
   
           /* no other constructors or methods implemented */
       }
   
   
       Vehicle a = new Bike ("green", 2);
       Vehicle b = new Car ("red", 4);
   
       I. b.wheels;
       II. a.getColor();
       III. b.numOfWheels();
       IV. a.color;