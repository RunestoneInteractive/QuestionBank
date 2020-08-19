.. mchoice:: mscope2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit5-Writing-Methods
   :subchapter: topic-5-2-method-parameters
   :topics: Unit5-Writing-Methods/topic-5-2-method-parameters
   :from_source: F
   :practice: T
   :answer_a: print1;
   :answer_b: print2;
   :answer_c: main;
   :correct: b
   :feedback_a: Method print1 accesses num, which is a formal parameter with method level scope.
   :feedback_b: Method print2 accesses age, which is not accessible since it is declared in the main method.
   :feedback_c: Method main accesses age, which is a local variable with method level scope..

   Which method has a scope error (i.e. uses a variable that is not visible in that method)?

   .. code-block:: java

      public class Visibility {

        public static void print1(int num) {
          System.out.println("num is " + num);
        }

        public static void print2() {
          System.out.println("age is " + age);
        }

        public static void main(String[] args) {
            int age = 20;
            print1(age);
            print2();
        }
      }