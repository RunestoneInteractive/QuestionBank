.. activecode:: class-Car
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit5-Writing-Classes
  :subchapter: topic-5-2-writing-constructors
  :topics: Unit5-Writing-Classes/topic-5-2-writing-constructors
  :from_source: T
  :language: java
  :autograde: unittest
  :practice: T
  :pct_on_first: 0.5
  :total_students_attempting: 204
  :num_students_correct: 198.0
  :mean_clicks_to_correct: 2.1212121212

  The following class defines a Car with the instance variables model and year, for example a Honda 2010 car. However, some of the code is missing. Fill in the code for the 2 constructors that are numbered 1 and 2. And fill in the code to call the constructors in the main method numbered 3. The car1 object should test the first constructor with default values and the car2 object should test the second constructor to create a Honda 2010 car. Run your program and make sure it works and prints out the information for both cars.
  ~~~~
  public class Car
  {
     //  instance variables
     private String model;
     private int year;
  
     // constructor: set instance variables to default values
     public Car()
     {
         // 1. set the instance variables to default values "" and 2019
  
  
     }
  
     // constructor: set instance variables to init parameters
     public Car(String initModel, int initYear)
     {
         // 2. set the instance variables to the init parameter variables
  
  
     }
  
     // Print Car info
     public void print()
     {
       System.out.println("Car model: " + model);
       System.out.println("Car year: " + year);
     }
  
     // main method for testing
     public static void main(String[] args)
     {
         // 3. call the constructor to create 2 new Car objects
         // using the 2 constructors.
         // car1 will be the default values.
         // car2 should be a Honda 2010 car.
         Car car1 =
         Car car2 =
  
         car1.print();
         car2.print();
     }
  }
  ====
  // Test Code for Lesson 5.2.0 - Car
    import static org.junit.Assert.*;
    import org.junit.After;
    import org.junit.Before;
    import org.junit.Test;
  
    import java.io.*;
  
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "Car model: \nCar year: 2019\nCar model: Honda\nCar year: 2010";
  
            boolean passed = getResults(expect, output, "Running main");
            assertTrue(passed);
        }
  
    }