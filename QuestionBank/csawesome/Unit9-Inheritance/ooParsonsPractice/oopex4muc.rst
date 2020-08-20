.. parsonsprob:: oopex4muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: ooParsonsPractice
   :topics: Unit9-Inheritance/ooParsonsPractice
   :from_source: F
   :adaptive: 
   :noindent: 
   :pct_on_first: 0.45
   :total_students_attempting: 20
   :num_students_correct: 19.0
   :mean_clicks_to_correct: 2.4736842105

   The following program should create an interface, named Person, with two methods, walk() and talk(). But, the blocks have been mixed up and may include extra blocks that are not needed in a correct solution. Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public interface Person {
   =====
   public abstract class Person { #distractor
   =====
   public class interface Person { #distractor
   =====
        public void walk() {
                System.out.println("walk");
        }
        public void talk() {
                System.out.println("talk");
        } #distractor
   =====
        public walk();
        public talk(); #distractor
   =====
        public void walk();
        public void talk();
   =====
   } // end class