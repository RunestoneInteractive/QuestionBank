.. clickablearea:: name_fields
    :author: bmiller
    :difficulty: 3.0
    :basecourse: apcsareview
    :chapter: JavaBasics
    :subchapter: partsOfAClass
    :topics: JavaBasics/partsOfAClass
    :from_source: T
    :question: Click on all the field declarations in the following class
    :iscode:
    :feedback: Remember, fields are private and are declared after the class declaration.

    :click-incorrect:public class Name {:endclick:

        :click-correct:private String first;:endclick:
        :click-correct:private String last;:endclick:

        :click-incorrect:public Name(String theFirst, String theLast) {:endclick:
            :click-incorrect:first = theFirst;:endclick:
            :click-incorrect:last = theLast;:endclick:
         :click-incorrect:}:endclick:

         :click-incorrect:public void setFirst(String theFirst) {:endclick:
            :click-incorrect:first = theFirst;:endclick:
         :click-incorrect:}:endclick:

         :click-incorrect:public void setLast(String theLast) {:endclick:
            :click-incorrect:first = theLast;:endclick:
         :click-incorrect:}:endclick:

    :click-incorrect:}:endclick: