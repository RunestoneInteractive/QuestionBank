.. mchoice:: qoo_7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: OOBasics
   :subchapter: ooInheritanceAccess
   :topics: OOBasics/ooInheritanceAccess
   :from_source: T
   :answer_a: currItem.setX(3);
   :answer_b: currItem.setY(2);
   :answer_c: currItem.x = 3;
   :answer_d: currItem.y = 2;
   :correct: c
   :feedback_a: The object currItem is an EnhancedItem object and it will inherit the public setX method from Item.
   :feedback_b: The object currItem is an EnhancedItem object and that class has a public setY method.
   :feedback_c: Even though an EnhancedItem object will have a x field the subclass does not have direct access to a private field.  Use the public setX method instead.
   :feedback_d: All code in the same class has direct access to all object fields.

   Given the following class definitions which of the following would not compile if it was used in place of the missing code in the main method?

   .. code-block:: java

      class Item
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

         public static void main(String[] args)
         {
            EnhancedItem currItem = new EnhancedItem();
            // missing code
         }
      }