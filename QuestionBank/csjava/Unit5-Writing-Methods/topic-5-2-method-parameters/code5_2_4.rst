.. activecode:: code5_2_4
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit5-Writing-Methods
  :subchapter: topic-5-2-method-parameters
  :topics: Unit5-Writing-Methods/topic-5-2-method-parameters
  :from_source: T
  :language: java

  Use the CodeLens button to watch how the square method
  alters the value of x, while the value of y in the main method is not affected.

  Try changing the name of the variable in the main method to "x" and rerun the program.  You should see
  that the variable in the main method remains unaffected by changes made in the square method, even when
  the variables have the same name.
  ~~~~
  public class CallByValue
  {
    public static void square(int x)
    {
      x = x * x;
      System.out.println(x);
    }

    public static void main(String[] args)
    {
      int y = 5;
      square(y);
      System.out.println(y);
    }
  }