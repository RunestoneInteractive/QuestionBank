.. activecode:: SuperEx
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: OOBasics
   :subchapter: ooSuper
   :topics: OOBasics/ooSuper
   :from_source: T
   :language: java

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