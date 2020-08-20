.. activecode:: javaelif2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: java4python
   :chapter: Java4Python
   :subchapter: conditionals
   :topics: Java4Python/conditionals
   :from_source: T
   :language: java
   :sourcefile: ElseIf.java

   public class ElseIf {
       public static void main(String args[]) {
        int grade = 85;
        if (grade < 60) {
            System.out.println('F');
        } else if (grade < 70) {
            System.out.println('D');
        } else if (grade < 80) {
            System.out.println('C');
        } else if (grade < 90) {
            System.out.println('B');
        } else  System.out.println('A');
       }
   }