.. activecode:: PersonClassThis
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit6-Writing-Classes
  :subchapter: topic-6-9-this
  :topics: Unit6-Writing-Classes/topic-6-9-this
  :from_source: F
  :language: java

  Observe the use of the keyword this in the code below.
  ~~~~
  public class Person
  {
     // instance variables
      private String name;
      private String email;
      private String phoneNumber;

     // constructor
     public Person(String theName)
     {
        this.name = theName;
     }

     // accessor methods - getters
     public String getName() { return this.name;}
     public String getEmail() { return this.email;}
     public String getPhoneNumber() { return this.phoneNumber;}

     // mutator methods - setters
     public void setName(String theName) { this.name = theName;}
     public void setEmail(String theEmail) {this.email = theEmail;}
     public void setPhoneNumber(String thePhoneNumber) { this.phoneNumber = thePhoneNumber;}
     public String toString()
     {
        return this.name + " " + this.email + " " + this.phoneNumber;
     }

     // main method for testing
     public static void main(String[] args)
     {
        Person p1 = new Person("Sana");
        System.out.println(p1);
        Person p2 = new Person("Jean");
        p2.setEmail("jean@gmail.com");
        p2.setPhoneNumber("404 899-9955");
        System.out.println(p2);
     }
  }