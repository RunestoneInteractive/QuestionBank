.. mchoice:: qoo_8
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: topic-9-2-constructors
   :topics: Unit9-Inheritance/topic-9-2-constructors
   :from_source: F
   :answer_a: II only
   :answer_b: III only
   :answer_c: I and II only
   :answer_d: I, II, and III
   :correct: d
   :feedback_a: I is true because Point2D does have a no-arg constructor. II is true because Point2D does have a constructor that takes x and y. III is true because Point2D does have a no-arg constructor which will be called before the first line of code is executed in this constructor. The fields x and y are public in Point2D and thus can be directly accessed by all classes.
   :feedback_b: Point2D does have a constructor that takes an x and y value so this is okay. Also the call to super is the first line of code in the child constructor as required. However, both I and III are okay as well.
   :feedback_c: The x and y values in Point2D are public and so can be directly accessed by all classes including subclasses. Also there is a no-arg constructor in Point2D so the super no-arg constructor will be called before the first line of code in this constructor.
   :feedback_d: I is true because Point2D does have a no-arg constructor. II is true because Point2D does have a constructor that takes x and y. III is true because Point2D does have a no-arg constructor which will be called before the first line of code is executed in this constructor. The fields x and y are public in Point2D and thus can be directly accessed by all classes.
   :pct_on_first: 0.3
   :total_students_attempting: 30
   :num_students_correct: 30.0
   :mean_clicks_to_correct: 2.1333333333

   Given the class definitions of Point2D and Point3D below, which of the constructors that follow (labeled I, II, and III) would be valid in the Point3D class?
   
   .. code-block:: java
   
      class Point2D {
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
   
      // possible constructors for Point3D
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