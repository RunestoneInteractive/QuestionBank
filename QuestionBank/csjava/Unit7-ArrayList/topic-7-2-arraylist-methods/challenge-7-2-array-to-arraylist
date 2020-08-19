.. activecode:: challenge-7-2-array-to-arraylist
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/topic-7-2-arraylist-methods
   :from_source: T
   :language: java

   Rewrite the following code that uses an array to use an ArrayList instead. In the comments write why you think an ArrayList is a better data structure to use than an array for this problem.
   ~~~~
   import java.util.*;

   public class ToDoList
   {
      public static void main(String[] args)
      {
         // Rewrite this code to use an ArrayList instead of an array
         String[] toDoList = new String[3];
         toDoList[0] = "Do homework";
         toDoList[1] = "Help make dinner";
         toDoList[2] = "Call grandma";

         // changing element 1
         toDoList[1] = "Order pizza";

         System.out.println(toDoList.length + " things to do!");
         System.out.println("Here's the first thing to do: "
              + toDoList[0] );

         // remove item 0 and move everything down
         //  (this can be done in 1 command with ArrayList)
         toDoList[0] = toDoList[1];
         toDoList[1] = toDoList[2];
         toDoList[2] = "";

         System.out.println("Here's the next thing to do: "
              + toDoList[0] );

         // Why is an ArrayList better than an array for a toDoList?
         // Answer:
      }
   }