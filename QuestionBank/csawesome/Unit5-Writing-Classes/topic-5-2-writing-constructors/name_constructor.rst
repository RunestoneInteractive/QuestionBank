.. clickablearea:: name_constructor
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit5-Writing-Classes
    :subchapter: topic-5-2-writing-constructors
    :topics: Unit5-Writing-Classes/topic-5-2-writing-constructors
    :from_source: T
    :question: Click on all the lines of code that are part of constructors in the following class.
    :iscode: 
    :feedback: Constructors are public and have the same name as the class.
    :pct_on_first: 0.3332451032
    :total_students_attempting: 3778
    :num_students_correct: 3496.0
    :mean_clicks_to_correct: 3.3120709382

    :click-incorrect:public class Name {:endclick:
    
        :click-incorrect:private String first;:endclick:
        :click-incorrect:private String last;:endclick:
    
        :click-correct:public Name(String theFirst, String theLast) {:endclick:
            :click-correct:first = theFirst;:endclick:
            :click-correct:last = theLast;:endclick:
         :click-correct:}:endclick:
    
         :click-incorrect:public void setFirst(String theFirst) {:endclick:
            :click-incorrect:first = theFirst;:endclick:
         :click-incorrect:}:endclick:
    
         :click-incorrect:public void setLast(String theLast) {:endclick:
            :click-incorrect:last = theLast;:endclick:
         :click-incorrect:}:endclick:
    
    :click-incorrect:}:endclick: