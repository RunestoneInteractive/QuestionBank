.. activecode:: PersonLocalVar
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit6-Writing-Classes
  :subchapter: topic-6-8-scope-access
  :topics: Unit6-Writing-Classes/topic-6-8-scope-access
  :from_source: F
  :language: java

  public class Person
  {
     private String name;
     private String email;

     public Person(String initName, String initEmail)
     {
        name = initName;
        email = initEmail;
     }

     public String toString()
     {
       String name = "unknown";
       // The local variable name here will be used,
       //  not the instance variable name.
       return  name + ": " + email;
     }

     // main method for testing
     public static void main(String[] args)
     {
        // call the constructor to create a new person
        Person p1 = new Person("Sana", "sana@gmail.com");
        System.out.println(p1);
     }
  }