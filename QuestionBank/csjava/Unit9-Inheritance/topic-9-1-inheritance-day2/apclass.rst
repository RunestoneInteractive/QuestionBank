.. activecode:: apclass
  :author: bmiller
  :difficulty: 3
  :basecourse: csjava
  :topics: Unit9-Inheritance/topic-9-1-inheritance-day2
  :from_source: T
  :language: java

  What do you think the following code will print out?
  ~~~~
  import java.util.*;

    class Student
    {
      private String name;
      private int id;
    }

    class Course
    {
      private String title;
      private ArrayList<Student> roster;
    }

    public class APcourse extends Course
    {
       private String APexamDate;

       public static void main(String[] args)
       {
          APcourse csa = new APcourse();
          System.out.print("Is an APcourse a Course? ");
          System.out.println(csa instanceof Course);
       }
    }