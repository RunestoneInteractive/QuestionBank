.. activecode:: challenge-9-2-Square-Rectangle
  :author: bmiller
  :difficulty: 3
  :basecourse: csjava
  :topics: Unit9-Inheritance/topic-9-2-constructors
  :from_source: T
  :language: java

  Create a Square class that inherits from Rectangle.
  ~~~~
  class Rectangle
  {
      private int length;
      private int width;

      public Rectangle()
      {
         length = 1;
         width = 1;
      }

      public Rectangle(int l, int w)
      {
         length = l;
         width = w;
      }

      public void draw()
      {
        for(int i=0; i < length; i++)
        {
           for(int j=0; j < width; j++)
               System.out.print("* ");
            System.out.println();
        }
        System.out.println();
      }

  }

  // 1. Make the class square inherit from Rectangle
  public class Square
  {
       // 2. Add a Square no-argument constructor

       // 3. Add a Square constructor with 1 argument for a side

       public static void main(String[] args)
       {
          Rectangle r = new Rectangle(3,5);
          r.draw();
          // 4. Uncomment these to test
          // Square s1 = new Square();
          // s1.draw();
          // Square s = new Square(3);
          // s.draw();
       }
  }