.. mchoice:: qtnt4_18
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: Tests
   :subchapter: test4nt
   :topics: Tests/test4nt
   :from_source: T
   :answer_a: Having a constructor in the Student class that has a different parameter list than the constructor in the Person class.
   :answer_b: Having a sayName() method in Person and in Student.
   :answer_c: Having sayName() and sayName(String nickname) in the Student class.
   :answer_d: Having the changeGrade() method in the Student class.
   :answer_e: None of the above
   :correct: c
   :feedback_a: This is not an example of method overloading. In this constructor method, the parent constructor is called, but the method is not overloaded. Method overloading occurs when a class has two or more methods with the same name and a different parameter list (like a different number of parameters).
   :feedback_b: This is an example of method overridding, not method overloading. Method overridding occurs when a method is redefined in a subclass, and the method has the same parameter list. Method overloading occurs when there are two or more methods with the same name and different parameter lists in the same class.
   :feedback_c: In the Student class, there are two different sayName methods. The second sayName method has the same name and same return type, but the parameter lists differ. This is an example of method overloading.
   :feedback_d: This is just an example of adding new methods to the child class, that were not inherited from the parent class.
   :feedback_e: Method overloading occurs when a class has two or more methods with the same name and different parameters. There is a method in the Student class with the same name and two different parameter lists.

   The ``Person`` and ``Student`` classes are located below. Which of the following methods contains an example of method overloading?

   .. code-block:: java

      public class Person
      {
          private String name;
          private int age;

          public Person(String theName, int theAge)
          {
              name = theName;
              age = theAge;
          }

          public String sayName()
          {
              return name;
          }

          public int getAge()
          {
              return age;
          }
      }

      public class Student extends Person
      {
          private int grade;

          public Student(String theName, int theAge, int theGrade)
          {
              super (theName, theAge);
              grade = theGrade;
          }

          public String sayName()
          {
              return "My name is " + super.sayName();
          }

          public String sayName(String nickname)
          {
              return "My name is " + name + " but I like to be called " + nickname;
          }

          public int getGrade()
          {
              return grade;
          }

          public void changeGrade()
          {
              grade++;
          }
      }