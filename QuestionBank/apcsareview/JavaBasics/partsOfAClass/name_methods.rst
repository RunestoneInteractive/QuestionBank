.. clickablearea:: name_methods
    :author: bmiller
    :difficulty: 3.0
    :basecourse: apcsareview
    :chapter: JavaBasics
    :subchapter: partsOfAClass
    :topics: JavaBasics/partsOfAClass
    :from_source: T
    :question: Click on all the parts of the methods in the following class
    :iscode:
    :feedback: Methods follow the constructor.  They include a return type in case they returns something from the method.

    :click-incorrect:public class Name {:endclick:

        :click-incorrect:private String first;:endclick:
        :click-incorrect:private String last;:endclick:

        :click-incorrect:public Name(String theFirst, String theLast) {:endclick:
            :click-incorrect:first = theFirst;:endclick:
            :click-incorrect:last = theLast;:endclick:
         :click-incorrect:}:endclick:

         :click-correct:public void setFirst(String theFirst) {:endclick:
            :click-correct:first = theFirst;:endclick:
         :click-correct:}:endclick:

         :click-correct:public void setLast(String theLast) {:endclick:
            :click-correct:first = theLast;:endclick:
         :click-correct:}:endclick:

    :click-incorrect:}:endclick: