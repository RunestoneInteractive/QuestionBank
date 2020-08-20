.. activecode:: code5_2_3
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csjava
  :chapter: Unit5-Writing-Methods
  :subchapter: topic-5-2-method-parameters
  :topics: Unit5-Writing-Methods/topic-5-2-method-parameters
  :from_source: T
  :language: java

  Use the CodeLens button to step through the two method calls in the main.  Notice the ``inches`` and ``centimeters`` variables are
  visible in the ``inchesToCentimeters`` method but not the ``main`` method.
  ~~~~
  public class ScopeExample
  {
    public static void inchesToCentimeters(double inches)
    {
        double centimeters = inches * 2.54;
        System.out.println(inches + "-->" + centimeters);
    }

    public static void main(String[] args)
    {
        inchesToCentimeters(10);
        inchesToCentimeters(15.7);
    }

  }