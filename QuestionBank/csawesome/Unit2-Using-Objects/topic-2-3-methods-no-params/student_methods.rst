.. clickablearea:: student_methods
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-3-methods-no-params
    :topics: Unit2-Using-Objects/topic-2-3-methods-no-params
    :from_source: T
    :question: Click on the methods headers (signatures) in the following class. Do not click on the constructors.
    :iscode: 
    :feedback: Methods follow the constructors. The method header is the first line of a method.
    :pct_on_first: 0.2519053349
    :total_students_attempting: 2493
    :num_students_correct: 2295.0
    :mean_clicks_to_correct: 2.8845315904

    :click-incorrect:public class Student {:endclick:
    
        :click-incorrect:private String name;:endclick:
        :click-incorrect:private String email;:endclick:
    
        :click-incorrect:public Student(String initName, String intEmail) :endclick:
        :click-incorrect:{:endclick:
            :click-incorrect:name = initName;:endclick:
            :click-incorrect:email = initEmail;:endclick:
         :click-incorrect:}:endclick:
    
         :click-correct:public String getName() :endclick:
         :click-incorrect:{:endclick:
            :click-incorrect:return name;:endclick:
         :click-incorrect:}:endclick:
    
         :click-correct:public void print() :endclick:
         :click-incorrect:{:endclick:
            :click-incorrect:System.out.println(name + ":" + email);:endclick:
         :click-incorrect:}:endclick:
    :click-incorrect:}:endclick: