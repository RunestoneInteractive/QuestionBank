.. activecode:: code6_8_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit6-Writing-Classes
  :subchapter: topic-6-8-scope-access
  :topics: Unit6-Writing-Classes/topic-6-8-scope-access
  :from_source: T
  :language: java

  Try the following code to see that you cannot access the variables outside of their scope levels in the toString() method. Explain to someone sitting next to you why you can't access these. Try to fix the errors by either using variables that are in scope or moving the variable declarations so that the variables have larger scope.
  ~~~~
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
       for (int i=0; i < 5; i++) {
          int id = i;
       }
       // Can you access the blockScope variables i or id?
       System.out.println("i at the end of the loop is " + i);
       System.out.println("The last id is " + id);

       // Can toString() access parameter variables in Person()?
       return  initName + ": " + initEmail;
     }

     // main method for testing
     public static void main(String[] args)
     {
        // call the constructor to create a new person
        Person p1 = new Person("Sana", "sana@gmail.com");
        System.out.println(p1);
     }
  }