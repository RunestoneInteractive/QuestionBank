.. activecode:: InheritedGetSet
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit10-Inheritance
  :subchapter: topic-10-3-overriding
  :topics: Unit10-Inheritance/topic-10-3-overriding
  :from_source: T
  :language: java

  Demonstrated inherited get/set methods.
  ~~~~
  class Person
  {
     private String name;

     public String getName()
     {
        return name;
     }

     public boolean setName(String theNewName)
     {
        if (theNewName != null)
        {
           this.name = theNewName;
           return true;
        }
        return false;
     }
  }

  public class Employee extends Person
  {

     private static int nextId = 1;
     private int id;

     public Employee()
     {
        id = nextId;
        nextId++;
     }

     public int getId()
     {
        return id;
     }

     public static void main(String[] args)
     {
        Employee emp = new Employee();
        emp.setName("Dina");
        System.out.println(emp.getName());
        System.out.println(emp.getId());
     }
  }