.. activecode:: code1_4_9
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-4-assignment
   :topics: Unit1-Getting-Started/topic-1-4-assignment
   :from_source: T
   :language: java
   :stdin: Fred Smith

   Run this program to read in a name from the input stream.
   You can type a different name in the input window shown below the code.

   Try stepping through the code with the CodeLens tool to see how the name variable is assigned to the value read by the scanner.
   ~~~~

    import java.util.Scanner;
    public class NameReader {

        public static void main(String[] args) {

            Scanner scan = new Scanner(System.in);

            System.out.println("Please Enter your name: ");
            String name = scan.nextLine();
            System.out.println("Hello " + name);

        }

    }