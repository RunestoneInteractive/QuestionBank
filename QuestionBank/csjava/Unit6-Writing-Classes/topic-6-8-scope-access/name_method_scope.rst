.. clickablearea:: name_method_scope
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit6-Writing-Classes
    :subchapter: topic-6-8-scope-access
    :topics: Unit6-Writing-Classes/topic-6-8-scope-access
    :from_source: F
    :question: Click on all the variable declarations that are at Method Level Scope.
    :iscode:
    :feedback: Remember that the parameter variables and the local variables declared inside a method have Method Level Scope.

    :click-incorrect:public class Name {:endclick:

        :click-incorrect:private String first;:endclick:
        :click-incorrect:public String last;:endclick:

        :click-correct:public Name(String theFirst, String theLast) {:endclick:
            :click-correct:String firstName = theFirst;:endclick:
            :click-incorrect:first = firstName;:endclick:
            :click-incorrect:last = theLast;:endclick:
         :click-incorrect:}:endclick:
    :click-incorrect:}:endclick: