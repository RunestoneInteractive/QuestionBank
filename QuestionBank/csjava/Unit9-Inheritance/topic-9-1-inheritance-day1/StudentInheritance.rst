.. activecode:: StudentInheritance
  :author: bmiller
  :difficulty: 3
  :basecourse: csjava
  :topics: Unit9-Inheritance/topic-9-1-inheritance-day1
  :from_source: T
  :language: java

  What do you need to add to the Student class declaration below to make it inherit from type Person? When you fix the code, the **instanceof** operator will return true that Student s is an instance of both the Student and the Person class. What other private instance variables could you add to Person and Student? In which class would you put an address attribute? Where would you put gpa?
  ~~~~
    class Person
    {
       private String name;
    }

    // How can we make the Student class inherit from class Person?
    public class Student
    {
       private int id;

       public static void main(String[] args)
       {
          Student s = new Student();
          System.out.println(s instanceof Student);
          System.out.println(s instanceof Person);
       }
    }