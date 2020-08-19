.. activecode:: superclassArray
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit9-Inheritance
  :subchapter: topic-9-5-hierarchies
  :topics: Unit9-Inheritance/topic-9-5-hierarchies
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.125
  :total_students_attempting: 8
  :num_students_correct: 6.0
  :mean_clicks_to_correct: 3.6666666667

  Scroll down to look at the Dog class and add a similar Cat class that extends Pet. Don't make the Cat class public because there can only be 1 public class in a file. Scroll back to the main method and add some Cat objects to the ArrayList too. Does the petList work with Cats too?
  ~~~~
  import java.util.*; // for ArrayList
  
   public class Pet
   {
       private String name;
       private String type;
  
       public Pet(String n, String t)
       {
          name = n;
          type = t;
       }
       public String toString()
       {
          return name + " is a " + type;
       }
  
       public static void main(String[] args)
       {
           ArrayList<Pet> petList = new ArrayList<Pet>();
           petList.add(new Pet("Sammy","hamster"));
           petList.add(new Dog("Fido"));
           // This loop will work for all subclasses of Pet
           for(Pet p : petList)
           {
              System.out.println(p);
           }
       }
    }
    class Dog extends Pet
    {
       public Dog(String n)
       {
         super(n, "dog");
       }
    }
    ====
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
  
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("Pet");
        }
  
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "Sammy is a hamster\nFido is a dog";
  
            boolean passed = getResults(expect, output, "Running main", true);
            assertTrue(passed);
  
        }
  
        @Test
        public void test2()
        {
            String output = getMethodOutput("main");
            String expect = "Sammy is a hamster\nFido is a dog\n... is a cat";
  
            boolean passed = output.contains("is a cat");
  
            getResults(expect, output, "Checking that a cat was added to the output", passed);
            assertTrue(passed);
  
        }
  
        @Test
        public void test3()
        {
            String target = "class Cat";
  
            boolean passed = checkCodeContains(target);
            assertTrue(passed);
  
        }
  
        @Test
        public void test4()
        {
            String target = "public Cat(String *)";
  
            boolean passed = checkCodeContains(target);
            assertTrue(passed);
  
        }
  
        @Test
        public void test5()
        {
            String target = "petList.add(new Cat(";
  
            boolean passed = checkCodeContains(target);
            assertTrue(passed);
  
        }
    }