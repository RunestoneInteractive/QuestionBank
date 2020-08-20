.. mchoice:: qoo_10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit10-Inheritance
   :subchapter: topic-10-6-polymorphism
   :topics: Unit10-Inheritance/topic-10-6-polymorphism
   :from_source: T
   :practice: T
   :answer_a: Shape Shape Shape Shape
   :answer_b: Shape Rectangle Square Circle
   :answer_c: There will be a compile time error
   :answer_d: Shape Rectangle Rectangle Circle
   :answer_e: Shape Rectangle Rectangle Oval
   :correct: d
   :feedback_a: The Rectangle subclass of Shape overrides the what method so this can't be right.
   :feedback_b: The Square subclass doesn't not override the what method so it will use the one in Rectangle.
   :feedback_c: This code will compile.  The declared type can hold objects of that type or any subclass of the type.
   :feedback_d: The Shape object will print Shape.  The Rectangle object will print Rectangle.  The Square object will also print Rectangle since it doesn't overrride the what method.  The Circle object will print Circle.
   :feedback_e: The Circle class does override the what method so this can't be right.

   What is the output from running the main method in the Shape class?

   .. code-block:: java

      public class Shape {
         public void what() { System.out.print("Shape ");}

         public static void main(String[] args) {

            Shape[] shapes = {new Shape(), new Rectangle(), new Square(),
                              new Circle()};
            for (Shape s : shapes)
            {
               s.what();
               System.out.print(" ");
            }
         }

      }

      class Rectangle extends Shape {
         public void what() { System.out.print("Rectangle "); }
      }

      class Square extends Rectangle {
      }

      class Oval extends Shape {
         public void what() { System.out.print("Oval "); }
      }

      class Circle extends Oval {
         public void what() { System.out.print("Circle ");}
      }