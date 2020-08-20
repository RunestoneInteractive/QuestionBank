.. mchoice:: qsh_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: ooMedMC
   :topics: Unit9-Inheritance/ooMedMC
   :from_source: T
   :practice: T
   :random: 
   :answer_a: Lasagna Meow Screeech
   :answer_b: Meow Screeech Lasagna
   :answer_c: Screeech Meow Lasagna
   :answer_d: Lasagna Screeech Meow
   :correct: b
   :feedback_a: The baseclass constructor runs first so Animal doesn't have one so then it goes to Cat's constructor and then Garfield's constructor
   :feedback_b: The baseclass constructor runs first so Animal doesn't have one so then it goes to Cat's constructor and then Garfield's constructor
   :feedback_c: The baseclass constructor runs first so Animal doesn't have one so then it goes to Cat's constructor and then Garfield's constructor
   :feedback_d: The baseclass constructor runs first so Animal doesn't have one so then it goes to Cat's constructor and then Garfield's constructor
   :pct_on_first: 0.2433628319
   :total_students_attempting: 678
   :num_students_correct: 666.0
   :mean_clicks_to_correct: 2.6891891892

   What is the output of the following code?
   
   .. code-block:: java
   
    class Animal
    {
        void someSound()
        {
            System.out.print("Screeech ");
        }
    }
   
    class Cat extends Animal
    {
        public Cat()
        {
            System.out.print("Meow ");
            super.someSound();
        }
    }
   
    class Garfield extends Cat
    {
        public Garfield()
        {
            System.out.print("Lasagna ");
        }
    }
    public class MainClass
    {
        public static void main(String[] args)
        {
            Garfield garfield = new Garfield();
        }
    }