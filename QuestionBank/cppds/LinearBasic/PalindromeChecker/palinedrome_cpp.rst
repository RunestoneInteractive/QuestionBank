.. activecode:: palinedrome_cpp
  :author: bmiller
  :difficulty: 3.0
  :basecourse: cppds
  :chapter: LinearBasic
  :subchapter: PalindromeChecker
  :topics: LinearBasic/PalindromeChecker
  :from_source: T
  :caption: Using a Deque to check palindromes
  :language: cpp

  //program that detects palindromes.

  #include <deque>
  #include <iostream>
  #include <string>

  using namespace std;

  bool palchecker(string aString) {
      deque<char> chardeque;
      int strLen = aString.length();
      for (int i = 0; i < strLen; i++) {
          //pushes each char in the string to the deque.
          chardeque.push_back(aString[i]);
      }

      bool stillEqual = true;

      while (chardeque.size() > 1 && stillEqual) {
          char first = chardeque.front();
          chardeque.pop_front();
          char last = chardeque.back();
          chardeque.pop_back();
          if (first != last) { //if the two opposite positions of the
                               //word is not the same, then it is not
                               //a palindrome.
              stillEqual = false;
          }
      }
      return stillEqual;
  }

  int main() {
      cout << palchecker("lsdkjfskf") << endl;
      cout << palchecker("radar") << endl;
  }