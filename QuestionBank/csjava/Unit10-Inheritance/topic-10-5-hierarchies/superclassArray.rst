.. activecode:: superclassArray
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit10-Inheritance
  :subchapter: topic-10-5-hierarchies
  :topics: Unit10-Inheritance/topic-10-5-hierarchies
  :from_source: T
  :language: java

  Scroll down to look at the Dog class and add a similar Cat class that extends Pet. Scroll back to the main method and add some Cat objects to the ArrayList too. Does the petList work with Cats too?
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