.. activecode:: InitPrivateInherited
  :author: bmiller
  :difficulty: 3.0
  :basecourse: apcsareview
  :chapter: OOBasics
  :subchapter: ooInheritanceAndConstructors
  :topics: OOBasics/ooInheritanceAndConstructors
  :from_source: T
  :language: java

  class Person
  {
     private String name;

     public Person(String theName)
     {
        this.name = theName;
     }

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

     public Employee(String theName)
     {
        super(theName);
        id = nextId;
        nextId++;
     }

     public int getId()
     {
        return id;
     }

     public static void main(String[] args)
     {
        Employee emp = new Employee("Mark");
        System.out.println(emp.getName());
        System.out.println(emp.getId());
     }
  }