.. activecode:: superclassMethod
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit10-Inheritance
  :subchapter: topic-10-5-hierarchies
  :topics: Unit10-Inheritance/topic-10-5-hierarchies
  :from_source: T
  :language: java

  Which toString() method is called below? What would happen if you commented out the Student toString() method? Which one would be called now?
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