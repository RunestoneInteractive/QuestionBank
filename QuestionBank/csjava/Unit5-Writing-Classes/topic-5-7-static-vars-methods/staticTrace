.. mchoice:: staticTrace
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit5-Writing-Classes/topic-5-7-static-vars-methods
   :from_source: T
   :practice: T

   Consider the class Temperature below which has a static variable. What is the output of the main method below?

   .. code-block:: java

       public class Temperature
       {
          private double temperature;
          public static double maxTemp = 0;

          public Temperature(double t)
          {
               temperature = t;
               if (t > maxTemp)
                   maxTemp = t;
          }

          public static void main(String[] args)
          {
               Temperature t1 = new Temperature(75);
               Temperature t2 = new Temperature(100);
               Temperature t3 = new Temperature(65);
               System.out.println("Max Temp: " + Temperature.maxTemp);
          }
        }

   - Max Temp: 0

     - maxTemp is changed in each call to the Temperature() constructor.

   - There is a compiler error because the static variable maxTemp cannot be used inside a non-static constructor.

     - Non-static methods and constructors can use any instance or static variables in the class.

   - Max Temp: 100

     + Yes, maxTemp is initialized to 0 and then changed to 75 and then 100 by the constructor calls.

   - Max Temp: 75

     - maxTemp will be changed to 100 by the second constructor call since 100 > 75.

   - Max Temp: 65

     - maxTemp will not be changed to 65 by the third constructor call because 67 is not > 100.