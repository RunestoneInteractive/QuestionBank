.. clickablearea:: name_class_scope
    :author: bmiller
    :difficulty: 3
    :basecourse: csjava
    :topics: Unit5-Writing-Classes/topic-5-8-scope-access
    :from_source: T
    :question: Click on all the variable declarations that are at Class Level Scope.
    :iscode:
    :feedback: Remember that the instance variables declared at the top of the class have Class Scope.

    :click-incorrect:public class Name {:endclick:

        :click-correct:private String first;:endclick:
        :click-correct:public String last;:endclick:

        :click-incorrect:public Name(String theFirst, String theLast) {:endclick:
            :click-incorrect:String firstName = theFirst;:endclick:
            :click-incorrect:first = firstName;:endclick:
            :click-incorrect:last = theLast;:endclick:
         :click-incorrect:}:endclick:
    :click-incorrect:}:endclick: