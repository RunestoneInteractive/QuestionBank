.. clickablearea:: greet_method_body
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit5-Writing-Methods
    :subchapter: topic-5-1-writing-methods
    :topics: Unit5-Writing-Methods/topic-5-1-writing-methods
    :from_source: F
    :question: Click on all statements contained within the greet method body.
    :iscode:
    :feedback: The greet method body consists of the 2 print statements nested between the curly braces that follow the method header

    :click-incorrect:public class Test2:endclick:
    :click-incorrect:{:endclick:
        :click-incorrect:public static void greet():endclick:
        :click-incorrect:{:endclick:
            :click-correct:System.out.println("Hello!");:endclick:
            :click-correct:System.out.println("How are you?");:endclick:
        :click-incorrect:}:endclick:
        :click-incorrect: :endclick:
        :click-incorrect:public static void main(String[] args):endclick:
        :click-incorrect:{:endclick:
            :click-incorrect:System.out.println("Before greeting");:endclick:
            :click-incorrect:greet();:endclick:
            :click-incorrect:System.out.println("After greeting");:endclick:
        :click-incorrect:}:endclick:
    :click-incorrect:}:endclick: