.. mchoice:: qooh_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit10-Inheritance
   :subchapter: ooHardMC
   :topics: Unit10-Inheritance/ooHardMC
   :from_source: T
   :practice: T
   :answer_a: II only
   :answer_b: III only
   :answer_c: I, II, and III
   :answer_d: I and II only
   :answer_e: I only
   :correct: c
   :feedback_a: <code>Point2D</code> does have a constructor that takes an <code>x</code> and <code>y</code> value so this is okay. Also the call to super is the first line of code in the child constructor as required. However, both I and III are okay as well.
   :feedback_b: The <code>x</code> and <code>y</code> values in <code>Point2D</code> are public and so can be directly accessed by all classes including subclasses. Also there is a no-arg constructor in <code>Point2D</code> so the super no-arg constructor will be called before the first line of code in this constructor.
   :feedback_c: I is true because <code>Point2D</code> does have a no-arg constructor. II is true because <code>Point2D</code> does have a constructor that takes <code>x</code> and <code>y</code>. III is true because <code>Point2D</code> does have a no-arg constructor which will be called before the first line of code is executed in this constructor. The fields <code>x</code> and <code>y</code> are public in <code>Point2D</code> and thus can be directly accessed by all classes.
   :feedback_d: This would be true if <code>x</code> and <code>y</code> were private in <code>Point2D</code>, but they are public.
   :feedback_e: <code>Point2D</code> does have a no-arg constructor and since the constructor in <code>Point3D</code> doesn't have an explicit call to super as the first line of code in the constructor one will be added for the no-arg constructor. However, both II and III are okay as well.

   If you have the following classes.  Which of the following constructors would be valid for ``Point3D``?

   .. code-block:: java

      public class Point2D {
         public int x;
         public int y;

         public Point2D() {}

         public Point2D(int x,int y) {
            this.x = x;
            this.y = y;
         }
        // other methods
      }

      public class Point3D extends Point2D
      {
         public int z;

         // other code
      }

      I.  public Point3D() {}
      II. public Point3D(int x, int y, int z)
          {
             super(x,y);
             this.z = z;
          }
      III. public Point3D(int x, int y)
           {
              this.x = x;
              this.y = y;
              this.z = 0;
           }