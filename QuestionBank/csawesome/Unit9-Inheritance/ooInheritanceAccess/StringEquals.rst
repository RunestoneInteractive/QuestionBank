.. activecode:: StringEquals
  :author: Brad Miller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit9-Inheritance
  :subchapter: ooInheritanceAccess
  :topics: Unit9-Inheritance/ooInheritanceAccess
  :from_source: F
  :language: java

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
        emp.setName("Mark");
        System.out.println(emp.getName());
        System.out.println(emp.getId());
     }
  }