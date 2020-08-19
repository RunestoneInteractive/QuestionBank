.. activecode:: superclassMethodKA
  :author: Katie Anderson
  :difficulty: 0.0
  :basecourse: csawesome
  :chapter: Unit9-Inheritance
  :subchapter: topic-9-5-hierarchies
  :topics: Unit9-Inheritance/topic-9-5-hierarchies
  :from_source: F
  :language: java

  Which toString() method is called below? What would happen if you commented out the Student toString() method? Which one would be called now?
  Scroll down to the bottom to answer these questions.
  ~~~~
  public class Tester
  {
       // This will implicitly call the toString() method of object p
       public void print(Person p)
       {
          System.out.println(p);
       }
       public static void main(String[] args)
       {
          Person p = new Person("Sila");
          Student s = new Student("Tully", 1001);
          Tester t = new Tester();
          t.print(p); //call print with a Person
          t.print(s); //call print with a Student
       }
    }

    class Person
    {
       private String name;
       public Person(String name)
       {
          this.name = name;
       }
       public String toString()
       {
          return name;
       }
    }

    class Student extends Person
    {
       private int id;
       public Student(String name, int id)
       {
          super(name);
          this.id = id;
       }
       public String toString()
       {
          return super.toString() + " " + id;
       }
    }

/* Answer the following questions below.  
 * comment out your answers so the code will run
 */

//1. Which toString() is called on line 13?

//2.  Which toString() is called on line 14?

//3.  What would happen if you commented out the Student toString() method?  
//    Which toString() method would be called now? Try it first, then answer.