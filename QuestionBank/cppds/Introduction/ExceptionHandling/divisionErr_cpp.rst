.. activecode:: divisionErr_cpp
  :author: Brad Miller
  :difficulty: 3.0
  :basecourse: cppds
  :chapter: Introduction
  :subchapter: ExceptionHandling
  :topics: Introduction/ExceptionHandling
  :from_source: F
  :caption: Error Handling for Division
  :language: cpp

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

      } catch (const char *err) {
              // If an error is thrown, print it
              cout << err;
      }

      return 0;
  }