.. clickablearea:: name_constructor
    :author: bmiller
    :difficulty: 3.0
    :basecourse: apcsareview
    :chapter: JavaBasics
    :subchapter: partsOfAClass
    :topics: JavaBasics/partsOfAClass
    :from_source: T
    :question: Click on all the parts of the contsructor
    :iscode:
    :feedback: Constructors are public and have the same name as the class.

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
            :click-incorrect:first = theLast;:endclick:
         :click-incorrect:}:endclick:

    :click-incorrect:}:endclick: