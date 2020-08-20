.. activecode:: GregorianCalendar1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-2-constructors
    :topics: Unit2-Using-Objects/topic-2-2-constructors
    :from_source: F
    :language: java

    Run the code below to see what it does. Note that the code below will return the current date and time on the server which might be different from the time where you are.
    ~~~~
    import java.util.GregorianCalendar;

    public class Test1
    {
        public static void main(String[] args)
        {
            GregorianCalendar today = new GregorianCalendar();
            System.out.println("Current date and time on server: "
                         + today.getTime());
        }
     }