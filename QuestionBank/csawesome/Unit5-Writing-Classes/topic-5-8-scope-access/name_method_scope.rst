.. clickablearea:: name_method_scope
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit5-Writing-Classes
    :subchapter: topic-5-8-scope-access
    :topics: Unit5-Writing-Classes/topic-5-8-scope-access
    :from_source: T
    :question: Click on all the variable declarations that are at Method Level Scope.
    :iscode: 
    :feedback: Remember that the parameter variables and the local variables declared inside a method have Method Level Scope.
    :pct_on_first: 0.051200565
    :total_students_attempting: 2832
    :num_students_correct: 2614.0
    :mean_clicks_to_correct: 3.700841622

    :click-incorrect:public class Name {:endclick:
    
        :click-incorrect:private String first;:endclick:
        :click-incorrect:public String last;:endclick:
    
        :click-correct:public Name(String theFirst, String theLast) {:endclick:
            :click-correct:String firstName = theFirst;:endclick:
            :click-incorrect:first = firstName;:endclick:
            :click-incorrect:last = theLast;:endclick:
         :click-incorrect:}:endclick:
    :click-incorrect:}:endclick: