.. activecode:: OverrideEquals
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit9-Inheritance/topic-9-7-Object
   :from_source: T
   :language: java

   Try to guess what this code will print out before running it.
   ~~~~
   public class Person
   {
      private String name;

      public Person(String theName)
      {
         this.name = theName;
      }

      /** Overriden equals method that checks if names are equal
          in this Person object and an the other Object.
          */
      public boolean equals(Object other)
      {
         // Type cast other to a Person
         Person otherPerson = (Person) other;
         // Check if names are equal
         return this.name.equals(otherPerson.name);
      }

      public static void main(String[] args)
      {
         Person p1 = new Person("Gabe");
         Person p2 = new Person("Gus");
         Person p3 = new Person("Gabe");
         Person p4 = p3;
         System.out.println(p1.equals(p2));
         System.out.println(p2.equals(p3));
         System.out.println(p1.equals(p3));
         System.out.println(p3.equals(p4));
      }
   }