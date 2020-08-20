.. activecode:: code1_5_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-5-shortcutoperators
   :topics: Unit1-Getting-Started/topic-1-5-shortcutoperators
   :from_source: T
   :language: java

   What do you think is printed when the following code is executed?
   Try to guess the output before running the code.  You might be surprised at the result.
   Click on CodeLens to step through the  execution.
   Notice that the second println prints the original value 7 even though the memory
   location for variable ``count`` is updated to the value 8.
   ~~~~
    public class Postfix_Example {
        public static void main(String[] args) {
            int count = 7;
            System.out.println(count);
            System.out.println(count++);
            System.out.println(count);
        }
    }
   ====