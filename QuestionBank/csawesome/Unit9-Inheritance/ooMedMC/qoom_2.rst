.. mchoice:: qoom_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: ooMedMC
   :topics: Unit9-Inheritance/ooMedMC
   :from_source: T
   :practice: T
   :answer_a: I only
   :answer_b: II only
   :answer_c: I and II only
   :answer_d: II and III only
   :answer_e: I, II, and III
   :correct: d
   :feedback_a: I is wrong because <code>y</code> is a private field and thus can not be directly accessed from code in a client class.
   :feedback_b: I is wrong because <code>y</code>  is a private field and thus can not be directly accessed from code in a client class. II is correct because <code>EnhancedItem</code> has <code>setY</code> as a public method. III is correct because <code>EnhancedItem</code> inherits the public method <code>setX</code> from <code>Item</code>.
   :feedback_c: I is wrong because <code>y</code>  is a private field and thus can not be directly accessed from code in a client class.
   :feedback_d: I is wrong because <code>y</code>  is a private field and thus can not be directly accessed from code in a client class.  II is correct because <code>EnhancedItem</code> has <code>setY</code> as a public method.  III is correct because <code>EnhancedItem</code> inherits the public method <code>setX</code> from <code>Item</code>.
   :feedback_e: I is wrong because <code>y</code>  is a private field and thus can not be directly accessed from code in a client class.
   :pct_on_first: 0.5088919289
   :total_students_attempting: 731
   :num_students_correct: 718.0
   :mean_clicks_to_correct: 1.8509749304

   Given the following class declarations, and ``EnhancedItem enItemObj = new EnhancedItem();`` in a client class, which of the following statements would compile?
   
   .. code-block:: java
   
      public class Item
      {
         private int x;
   
         public void setX(int theX)
         {
            x = theX;
         }
         // ... other methods not shown
      }
   
      public class EnhancedItem extends Item
      {
         private int y;
   
         public void setY(int theY)
         {
            y = theY;
         }
   
        // ... other methods not shown
      }
   
      I. enItemObj.y = 32;
      II. enItemObj.setY(32);
      III. enItemObj.setX(52);