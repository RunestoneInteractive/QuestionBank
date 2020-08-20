.. activecode:: InitPrivateInherited
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit10-Inheritance
  :subchapter: topic-10-2-constructors
  :topics: Unit10-Inheritance/topic-10-2-constructors
  :from_source: T
  :language: java

  Try creating another Employee object in the main method that passes in your name and then use the get methods to print it out. Which class constructor sets the name? Which class constructor sets the id?
  ~~~~
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
        Employee emp = new Employee("Dani");
        System.out.println(emp.getName());
        System.out.println(emp.getId());
     }
  }