.. activecode:: toStringDemo
  :author: bmiller
  :difficulty: 3
  :basecourse: csjava
  :topics: Unit9-Inheritance/topic-9-7-Object
  :from_source: T
  :language: java

  After trying the code below, add another subclass called APStudent that extends Student with a new attribute called APscore and override the toString() method to call the superclass method and then add on the APscore. Create an APStudent object in the main method to test it.
  ~~~~
    public class Person
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
       public static void main(String[] args)
       {
          Person p = new Person("Sila");
          Student s = new Student("Tully", 1001);
          System.out.println(p); //call Person toString
          System.out.println(s);  //call Student toString
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