.. activecode:: while_loop_oob
  :author: bmiller
  :difficulty: 3.0
  :basecourse: apcsareview
  :chapter: LoopBasics
  :subchapter: lMistakes
  :topics: LoopBasics/lMistakes
  :from_source: T
  :language: java

  public class Test
  {
     public static void main(String[] args)
     {
         String result = "";
         String message = "watch out";
         int pos = 0;
         while (pos < message.length())
         {
            result = result + message.substring(pos,pos+2);
            pos = pos + 1;
         }
         System.out.println(result);
     }
  }