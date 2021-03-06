.. mchoice:: qoom_5
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit9-Inheritance/ooMedMC
   :from_source: T
   :practice: T
   :answer_a: The code compiles and runs with no errors, the output is 5 6 5 6
   :answer_b: The code compiles and runs with no errors, the output is: 5 6 10 11
   :answer_c: The code compiles and runs with no errors, the output is 10 11 10 11
   :answer_d: The code won't compile.
   :answer_e: You get a runtime error <code>ClassCastException</code>, when <code>fastCar.addFuel()</code> is executed.
   :correct: b
   :feedback_a: <code>RaceCar</code>, while it inherits methods from <code>Car</code> via inheritance, has a separate and different constructor that sets the initial fuel amount to <code>2 * g</code>, thus in this case, <code>fuel</code> for <code>fastCar</code> is set to <code>10</code> initially.
   :feedback_b: The code compiles correctly, and because <code>RaceCar</code> extends the <code>Car</code> class, all the public methods of <code>Car</code> can be used by <code>RaceCar</code> objects. Also, a variable <code>Car</code> can refer to a <code>Car</code> object or an object of any subclass of <code>Car</code>. An object always knows the class that created it, so even though <code>fastCar</code> is declared to be a <code>Car</code> the constructor that is executed is the one for <code>RaceCar</code>.
   :feedback_c: The variable <code>car</code> is a <code>Car</code> object, so the constructor used is not the same as the <code>fastCar</code> object which is a <code>RaceCar</code>. The <code>car</code> constructor does not change the passed in parameter, so it is set to <code>5</code> initially.
   :feedback_d: <code>RaceCar</code> inherits from the <code>Car</code> class so all the public methods in <code>Car</code> can be accessed by any object of the <code>RaceCar</code> class.
   :feedback_e: <code>RaceCar</code> inherits from the <code>Car</code> class so all the public methods in <code>Car</code> can be accessed by any object of the <code>RaceCar</code> class.

   Given the following class declarations and code, what is the result when the code is run?

   .. code-block:: java

      public class Car
      {
         private int fuel;

         public Car() { fuel = 0; }
         public Car(int g) { fuel = g; }

         public void addFuel() { fuel++; }
         public void display() { System.out.print(fuel + " "); }
      }

      public class RaceCar extends Car
      {
         public RaceCar(int g) { super(2*g); }
      }

      What is the result when the following code is compiled and run?

      Car car = new Car(5);
      Car fastCar = new RaceCar(5);
      car.display()
      car.addFuel();
      car.display();
      fastCar.display();
      fastCar.addFuel();
      fastCar.display();