.. activecode:: getting_user_input_AC_1
  :author: bmiller
  :difficulty: 3.0
  :basecourse: thinkcpp
  :chapter: Chapter8
  :subchapter: getting_user_input
  :topics: Chapter8/getting_user_input
  :from_source: T
  :language: cpp
  :stdin: 42

  The active code below is an example of what getting input from the
  user might look like. Feel free to change 42 to other values!
  ~~~~
  #include <iostream>
  using namespace std;

  int main () {
      int x;

      // prompt the user for input
      cout << "Enter an integer: ";

      // get input
      cin >> x;

      // check and see if the input statement succeeded
      if (cin.good() == false) {
          cout << "That was not an integer." << endl;
          return -1;
      }

      // print the value we got from the user
      cout << x << endl;
      return 0;
  }