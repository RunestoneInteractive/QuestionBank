.. activecode:: challenge-9-3-Pet-Sounds
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: topic-9-3-overriding
   :topics: Unit9-Inheritance/topic-9-3-overriding
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.0
   :total_students_attempting: 7
   :num_students_correct: 5.0
   :mean_clicks_to_correct: 3.0

   Complete the Dog and Cat classes below to inherit from Pet with a constructor and a method speak() that prints out ``Woof!`` or ``Meow!``.
   ~~~~
   public class Pet
   {
       private String name;
       private String type;
   
       public Pet(String n, String t)
       {
          name = n;
          type = t;
       }
       public String getType(){
         return type;
       }
       public String getName(){
         return name;
       }
   
       public void speak()
       {
         System.out.println("grr!");
       }
       public static void main(String[] args)
       {
           Pet p = new Pet("Sammy","hamster");
           System.out.println(p.getType());
           p.speak();
   
          /* Dog d = new Dog("Fido");
           System.out.println(d.getType());
           d.speak();
           Cat c = new Cat("Fluffy");
           System.out.println(c.getType());
           c.speak();
           */
       }
    }
   
    // Complete the Dog class
    class Dog
    {
   
   
    }
   
    // Add a Cat class
   
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
            String expect = "hamster\ngrr!\ndog\nWoof!\ncat\nMeow!\n";
   
            boolean passed = getResults(expect, output, "Running main");
            assertTrue(passed);
        }
   
        @Test
        public void test2()
        {
            String code = getCode();
            String target = "extends Pet";
   
            int num = countOccurences(code, target);
   
            boolean passed = num >= 2;
            getResults("2", ""+num, "Testing code for " + target, passed);
            assertTrue(passed);
        }
   
        @Test
        public void test3()
        {
            String code = getCode();
            String target = "public void speak()";
   
            int num = countOccurences(code, target);
   
            boolean passed = num >= 2;
            getResults("2", ""+num, "Testing code for " + target, passed);
            assertTrue(passed);
        }
   
        @Test
        public void test4()
        {
            String code = getCode();
            String target = "super(";
   
            int num = countOccurences(code, target);
            boolean passed = num >= 2;
            getResults("2", ""+num, "Testing code for " + target);
            assertTrue(passed);
        }
    }