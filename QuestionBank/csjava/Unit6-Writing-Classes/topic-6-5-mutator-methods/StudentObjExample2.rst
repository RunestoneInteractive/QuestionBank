.. activecode:: StudentObjExample2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit6-Writing-Classes
  :subchapter: topic-6-5-mutator-methods
  :topics: Unit6-Writing-Classes/topic-6-5-mutator-methods
  :from_source: F
  :language: java

  Fix the main method to include a call to the appropriate set method.
  ~~~~
  public class TesterClass
  {
     // main method for testing
     public static void main(String[] args)
     {
        Student s1 = new Student("Skyler", "skyler@sky.com", 123456);
        System.out.println(s1);
        s1.setName("Skyler 2");
        // Main doesn't have access to email, use set method!
        s1.email = "skyler2@gmail.com";
        System.out.println(s1);
     }
   }

  class Student
  {
     private String name;
     private String email;
     private int id;

     public Student(String initName, String initEmail, int initId)
     {
        name = initName;
        email = initEmail;
        id = initId;
     }
     // mutator methods - setters
     public void setName(String newName)
     {
       name = newName;
     }
     public void setEmail(String newEmail)
     {
       email = newEmail;
     }
     public void setId(int newId)
     {
       id = newId;
     }
     // accessor methods - getters
     public String getName()
     {
        return name;
     }
     public String getEmail()
     {
        return email;
     }
     public int getId()
     {
        return id;
     }
     public String toString() {
        return id + ": " + name + ", " + email;
     }
  }