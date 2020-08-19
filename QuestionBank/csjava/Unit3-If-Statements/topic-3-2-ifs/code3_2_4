.. activecode:: code3_2_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-2-ifs
   :topics: Unit3-If-Statements/topic-3-2-ifs
   :from_source: T
   :language: java
   :stdin: 16 0


   Run the program to confirm that it fails when a value of 0 is entered for numPeople (second input value).
   ~~~~
    import java.util.Scanner;
    public class PizzaCalculatorInput {

        public static void main(String[] args) {
            int pizzaSlices, numPeople, slicesPerPerson, leftoverSlices;
            Scanner scan = new Scanner(System.in);
            pizzaSlices = scan.nextInt();
            numPeople = scan.nextInt();
            slicesPerPerson = pizzaSlices / numPeople;
            leftoverSlices = pizzaSlices % numPeople;
            System.out.println(slicesPerPerson);
            System.out.println(leftoverSlices);
        }

    }