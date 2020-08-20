.. activecode:: postfixeval_cpp
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cppds
  :chapter: LinearBasic
  :subchapter: InfixPrefixandPostfixExpressions
  :topics: LinearBasic/InfixPrefixandPostfixExpressions
  :from_source: T
  :caption: Postfix evaluation
  :language: cpp

  //Solves a postfix math problem.

  #include <iostream>
  #include <stack>
  #include <string>

  using namespace std;

  int doMath(char op, int op1, int op2) {
      //Does math based on what op is passed as.
      if (op == '*') {
          return (op1 * op2);
      } else if (op == '/') {
          return (op1 / op2);
      } else if (op == '+') {
          return (op1 + op2);
      } else {
          return (op1 - op2);
      }
  }

  int postfixEval(string postfixExpr) {
      stack<int> operandStack;
      string nums = "0123456789";

      for (char i : postfixExpr) {
          if ((nums.find(i) <= nums.length())) { // Check if the current char is a number
              operandStack.push(int(i) - 48); // conversion from char to ascii
              // then subtract 48 to get the int value
              } else if (i != ' ') {
                            int operand2 = operandStack.top();
                            operandStack.pop();
                            int operand1 = operandStack.top();
                            operandStack.pop();
                            int result = doMath(i, operand1, operand2);
                            operandStack.push(result);
                    }
      }
      return operandStack.top();
  }

  int main() {
      cout << "7 8 + 3 2 + /" << endl;
      cout << postfixEval("7 8 + 3 2 + /") << endl;

      return 0;
  }