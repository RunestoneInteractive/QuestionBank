.. mchoice:: JP_AP2-3-4
    :author: John Pataracchia
    :difficulty: 0.0
    :basecourse: csawesome
    :chapter: Unit2-Using-Objects
    :subchapter: practice-test-objects
    :topics: Unit2-Using-Objects/practice-test-objects
    :from_source: F
    :random: 
    :pct_on_first: 0.6818181818
    :total_students_attempting: 44
    :num_students_correct: 43.0
    :mean_clicks_to_correct: 1.6744186047

    Consider the following class definition.
    
    .. code-block:: java
    
        public class Cat
        {
            public void meow()
            {
                System.out.print("Meow! Meow! ");
            }
    
            public void purr()
            {
                System.out.print("purrrrrrrr... ");
            }
    
            public void happy()
            {
                purr();
                meow();
            }
            /* Constructors not shown */
        }
    
    Which of the following code segments, if located in a method in a class other than Cat, will cause the message "purrrrrrrr... purrrrrrrr... Meow! Meow! " to be printed?
    
    - .. code-block:: java
    
        Cat a = new Cat();
        a.meow();
        a.purr();
    
      - This would print "Meow! Meow! purrrrrrrr... "
    
    - .. code-block:: java
    
        Cat a = new Cat();
        Cat.happy();
    
      - You must use the object a, not the class name Cat, to call its methods.
    
    - .. code-block:: java
    
        Cat a = new Cat();
        a.happy();
    
      - This would print out "purrrrrrrr... Meow! Meow! ".
    
    - .. code-block:: java
    
        Cat a = new Cat();
        a.purr();
        a.happy();
    
      + This would print out "purrrrrrrr... purrrrrrrr... Meow! Meow! ";
    
    - .. code-block:: java
    
         Cat a = new Cat();
         a.purr();
    
      - This would just print "purrrrrrrr... ".