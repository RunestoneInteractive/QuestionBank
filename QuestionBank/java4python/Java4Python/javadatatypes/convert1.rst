.. activecode:: convert1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: java4python
    :chapter: Java4Python
    :subchapter: javadatatypes
    :topics: Java4Python/javadatatypes
    :from_source: T
    :language: java
    :sourcefile: TempConv.java
    :stdin: 212

    import java.util.Scanner;

    public class TempConv {
        public static void main(String[] args) {
            Double fahr;
            Double cel;
            Scanner in;

            in = new Scanner(System.in);
            System.out.println("Enter the temperature in F: ");
            fahr = in.nextDouble();

            cel = (fahr - 32) * 5.0/9.0;
            System.out.println("The temperature in C is: " + cel);

            System.exit(0);
        }

    }