.. clickablearea:: stackclick
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: LinearBasic
    :subchapter: BalancedSymbolsGeneralCase
    :topics: LinearBasic/BalancedSymbolsGeneralCase
    :from_source: T
    :question: Using the program above, click on the line of code that adds an open parentheses to the stack.
    :iscode: 
    :feedback: Remember that the function to do this would be the push function.
    :pct_on_first: 0.5730337079
    :total_students_attempting: 89
    :num_students_correct: 80
    :mean_clicks_to_correct: 2.0375

    :click-incorrect:bool parChecker(string symbolString){:endclick:
          :click-incorrect:stack<string> s;:endclick:
          :click-incorrect:bool balanced = true;:endclick:
          :click-incorrect:int index = 0;:endclick:
          :click-incorrect:int symbolLength = symbolString.length();:endclick:
    
          while(index < symbolLength && balanced){
              :click-incorrect:string symbol;:endclick:
              :click-incorrect:symbol = symbolString[index];:endclick:
              :click-incorrect:string opens = "({[";:endclick:
              :click-incorrect:if (inString(symbol, opens)){:endclick:
                  :click-correct:s.push(symbol);:endclick:
              } else {
                  if (s.empty()){
                      :click-incorrect:balanced = false;:endclick:
                  } else {
                      :click-incorrect:string top = s.top();:endclick:
                      :click-incorrect:s.pop();:endclick:
                      :click-incorrect:if (!matches(top, symbol)){:endclick:
                          :click-incorrect:balanced = false;:endclick:
                      }
                  }
              }
              :click-incorrect:index = index + 1;:endclick:
          }
          :click-incorrect:if(balanced && s.empty()){:endclick:
              :click-incorrect:return true;:endclick:
          } else {
              :click-incorrect:return false;:endclick:
          }
    }