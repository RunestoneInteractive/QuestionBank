.. activecode:: divisionErr_cpp
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cpp4python
  :chapter: Exception_Handling
  :subchapter: ExceptionHandling
  :topics: Exception_Handling/ExceptionHandling
  :from_source: T
  :caption: Error Handling for Division
  :language: cpp

  // Shows exception handling using try,throw,
  // and catch in order to output
  // an error message to the console
  #include <iostream>
  using namespace std;

  double div(double num1, double num2) {
      if (num2 == 0) {
              // If the second number is 0, throw this error
              throw "Cannot divide by 0!\n";
      }

      return num1 / num2;
  }

  int main() {
      // Get input from the user
      float firstNum=10;
      float secondNum=0;

      try {
              // Attempt to divide the two numbers
              double result = div(firstNum, secondNum);
              cout << "result of division: " << result << endl;

      }
      catch (const char *err) {
              // If an error is thrown, print it
              cout << err;
      }

      return 0;
  }