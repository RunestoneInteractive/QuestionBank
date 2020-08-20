.. activecode:: ComparablePerson
   :author: Brad Miller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: ooComparable
   :topics: Unit9-Inheritance/ooComparable
   :from_source: F
   :language: java

   public class Person implements Comparable<Person>
   {
      private String firstName;
      private String lastName;
      private int age;

      public Person(String first, String last, int theAge)
      {
         this.firstName = first;
         this.lastName = last;
         this.age = theAge;
      }

      public int compareTo(Person other)
      {
         if (this.lastName.compareTo(other.lastName) == 0)
         {
            return this.firstName.compareTo(other.firstName);
         }
         else return this.lastName.compareTo(other.lastName);
      }

       public static void main(String[] args)
       {
          Person p1 = new Person("Karissa","Carter",17);
          Person p2 = new Person("Jayla", "Douglas",18);
          Person p3 = new Person("Anita", "Qin", 16);
          Person p4 = new Person("Carla", "Qin", 16);
          Person p5 = new Person("Carla", "Qin", 17);
          System.out.println(p1.compareTo(p2));
          System.out.println(p2.compareTo(p3));
          System.out.println(p3.compareTo(p1));
          System.out.println(p4.compareTo(p3));
          System.out.println(p4.compareTo(p5));
       }
   }