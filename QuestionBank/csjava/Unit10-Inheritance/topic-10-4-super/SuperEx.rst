.. activecode:: SuperEx
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit10-Inheritance
   :subchapter: topic-10-4-super
   :topics: Unit10-Inheritance/topic-10-4-super
   :from_source: T
   :language: java

   Add another subclass called Vegan that inherits from the Student class. Override the getFood() method to call the superclass getFood() but add a "No " in front of it and then add a vegan food. Change Javier to a Vegan and try it out!
   ~~~~
   public class Person
   {
         private String name = null;

         public Person(String theName)
         {
            name = theName;
         }

         public String getFood()
         {
            return "Hamburger";
         }

         public static void main(String[] args)
         {
            Person p = new Student("Javier");
            System.out.println(p.getFood());
         }
      }

      class Student extends Person
      {
         private int id;
         private static int nextId = 0;

         public Student(String theName)
         {
           super(theName);
           id = nextId;
           nextId++;
         }

         public String getFood()
         {
            String output = super.getFood();
            return output + " and Taco";
         }

         public int getId() {return this.id;}
         public void setId (int theId)
         {
            this.id = theId;
         }
      }