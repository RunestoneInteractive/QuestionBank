.. activecode:: javaswitch
   :author: bmiller
   :difficulty: 3.0
   :basecourse: java4python
   :chapter: Java4Python
   :subchapter: conditionals
   :topics: Java4Python/conditionals
   :from_source: T
   :language: java
   :sourcefile: SwitchUp.java

   public class SwitchUp {
       public static void main(String args[]) {
        int grade = 85;

        int tempgrade = grade / 10;
        switch(tempgrade) {
        case 10:
        case 9:
            System.out.println('A');
            break;
        case 8:
            System.out.println('B');
            break;
        case 7:
            System.out.println('C');
            break;
        case 6:
            System.out.println('A');
            break;
        default:
            System.out.println('F');
        }
      }
    }