.. activecode:: DieExample
  :author: bmiller
  :difficulty: 3.0
  :basecourse: apcsareview
  :chapter: OOBasics
  :subchapter: objectsAndClasses
  :topics: OOBasics/objectsAndClasses
  :from_source: T
  :language: java

  public class Die
  {
     private int lastValue;

     public int roll()
     {
        lastValue = (int) (Math.random() * 6) + 1;
        return lastValue;
     }

     public static void main(String[] args)
     {
        Die d = new Die();
        for (int i = 0; i < 10; i++)
        {
           System.out.println(d.roll());
        }
     }
   }