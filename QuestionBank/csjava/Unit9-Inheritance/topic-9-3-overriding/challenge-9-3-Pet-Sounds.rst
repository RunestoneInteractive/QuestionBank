.. activecode:: challenge-9-3-Pet-Sounds
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit9-Inheritance/topic-9-3-overriding
   :from_source: T
   :language: java

   Complete the Dog and Cat classes below to inherit from Pet with a constructor and a method speak() that prints out "Woof!" or "Meow!".
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