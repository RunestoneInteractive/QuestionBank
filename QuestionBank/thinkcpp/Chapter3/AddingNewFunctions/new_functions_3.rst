.. clickablearea:: new_functions_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter3
   :subchapter: AddingNewFunctions
   :topics: Chapter3/AddingNewFunctions
   :from_source: T
   :question: Click on all function CALLS.
   :iscode: 
   :feedback: Remember, the operator '=' is used for assignment.
   :pct_on_first: 1.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.0

   :click-incorrect:void printX() {:endclick:
       :click-incorrect:cout << "X";:endclick:
   }
   
   :click-incorrect:void printVar(int a) {:endclick:
       :click-incorrect:cout << a;:endclick:
   }
   
   :click-incorrect:int main() {:endclick:
       :click-incorrect:int x = 7;:endclick:
       :click-correct:printVar(x);:endclick:
       :click-incorrect:if (x < 10) {:endclick:
           :click-incorrect:x = x - 1;:endclick:
       }
       :click-correct:printX();:endclick:
       :click-incorrect:int y = 3;:endclick:
       :click-incorrect:double result = x / y;:endclick:
       :click-correct:printVar(result);:endclick:
       return 0;
   }