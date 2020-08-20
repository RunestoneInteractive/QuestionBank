.. activecode:: apclass
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit10-Inheritance
  :subchapter: topic-10-1-inheritance-day2
  :topics: Unit10-Inheritance/topic-10-1-inheritance-day2
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