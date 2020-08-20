.. clickablearea:: class_syntax
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: ObjectOrientedProgrammingDefiningClasses
    :topics: Introduction/ObjectOrientedProgrammingDefiningClasses
    :from_source: T
    :question: Click on the line where there is a syntax error when defining the following class
    :iscode: 
    :feedback: C++ class definitions end with a certain symbol
    :pct_on_first: 0.3109243697
    :total_students_attempting: 119
    :num_students_correct: 102
    :mean_clicks_to_correct: 5.5098039216

    :click-incorrect:class Fraction {:endclick:
      :click-incorrect:public::endclick:
          :click-incorrect:Fraction(int top, int bottom) {:endclick:
              :click-incorrect:/** Fraction contructor method */:endclick:
              :click-incorrect:num = top;     // setting num's value:endclick:
              :click-incorrect:den = bottom;  // setting den's value:endclick:
          :click-incorrect:}:endclick:
      :click-incorrect:private::endclick:
          :click-incorrect:int num; // num atribute:endclick:
          :click-incorrect:int den; // den attribute:endclick:
    :click-correct:}:endclick: