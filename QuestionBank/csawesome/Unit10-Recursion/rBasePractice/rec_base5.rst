.. clickablearea:: rec_base5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit10-Recursion
   :subchapter: rBasePractice
   :topics: Unit10-Recursion/rBasePractice
   :from_source: T
   :question: Click on the line or lines that contain the test for the base case
   :iscode: 
   :feedback: When a base case test is true a value is returned and the recursion stops
   :pct_on_first: 0.643902439
   :total_students_attempting: 410
   :num_students_correct: 395.0
   :mean_clicks_to_correct: 1.4253164557

   :click-incorrect:public static int mystery(String str):endclick:
   :click-incorrect:{:endclick:
       :click-correct:if (str.length() == 1) return 0;:endclick:
       :click-incorrect:else:endclick:
       :click-incorrect:{:endclick:
           :click-incorrect:if (str.substring(0,1).equals("y")) return 1 +:endclick:
                              :click-incorrect:mystery(str.substring(1));:endclick:
            :click-incorrect:else return mystery(str.substring(1));:endclick:
         :click-incorrect:}:endclick:
      :click-incorrect:}:endclick: