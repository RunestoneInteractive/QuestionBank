.. activecode:: while_loop_early_leave
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit4-Iteration
  :subchapter: topic-4-6-summary
  :topics: Unit4-Iteration/topic-4-6-summary
  :from_source: T
  :language: java

  public class Test
  {

     public static boolean isInOrder(String check)
     {
         int pos = 0;
         while (pos < check.length() - 1)
         {
            if (check.substring(pos, pos+1).compareTo(check.substring(pos+1, pos+2)) < 0)
               return true;
            pos++;
         }
         return false;
     }

     public static void main(String[] args)
     {
        System.out.println(isInOrder("abca"));
        System.out.println(isInOrder("abc"));

     }
  }