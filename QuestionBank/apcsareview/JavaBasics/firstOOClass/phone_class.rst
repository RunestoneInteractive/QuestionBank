.. clickablearea:: phone_class
    :author: bmiller
    :difficulty: 3.0
    :basecourse: apcsareview
    :chapter: JavaBasics
    :subchapter: firstOOClass
    :topics: JavaBasics/firstOOClass
    :from_source: T
    :question: Click on the class declaration (not the body of the class) in the following class definition.  Then click the "Check Me" button to see if you are correct or not.
    :iscode:
    :feedback: The class declaration starts the class.  It contains the keyword class in it.

    :click-correct:public class PhoneNumber {:endclick:

        :click-incorrect:private String country;:endclick:
        :click-incorrect:private String areaCode:endclick:
        :click-incorrect:private String number:endclick:

        :click-incorrect:public PhoneNumber(String theCountry, theArea, theNumber):endclick:
            :click-incorrect:country = theCountry;:endclick:
            :click-incorrect:areaCode = theArea;:endclick:
            :click-incorrect:number = theNumber;:endclick:
         :click-incorrect:}:endclick:

         :click-incorrect:public String getNumber() {:endclick:
            :click-incorrect:return number;:endclick:


         :click-incorrect:public void setNumber(String theNumber):endclick:
            :click-incorrect:number = theNumber;
         :click-incorrect:}:endclick:

    :click-incorrect:}:endclick: