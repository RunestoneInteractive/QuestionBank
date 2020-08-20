.. parsonsprob:: cpsc120_lab_q9
   :author: Matthew Zuniga
   :difficulty: 0.0
   :basecourse: cpp4python
   :chapter: Control_Structures
   :subchapter: Exercises
   :topics: Control_Structures/Exercises
   :from_source: F

   You are writing a program for an ATM that will validate the user's PIN. Here are some specifications:<br>
   <br>
   1. During the loop, ask the user to enter their PIN. If you enter your PIN incorrectly, increment the amount of attempts by 1.
   <br>
   2. If you fail to enter the PIN 3 times, you become locked out. (The program exits and tells the user the account has been locked)
   <br>
   3. If you enter the correct PIN, the program grants access and exits.
   <br>
   4. Assume the PIN is initialized at the start.

   -----
   int input = 0;
   int attempts = 0;
   int pin = 5555;
   =====
   do {
   cout << "Enter your PIN. " << endl;
   cin >> input;
   attempts++;
   =====
    if(input == pin) {
   =====
     cout << "You are logged in." << endl;
     attempts = 0;
     break;
    }
    cout << "Your PIN is incorrect. " << endl;
   =====
   }while(attempts != 3);
   =====
   #distractordo {
    cout << "Enter your PIN. " << endl;
    cin >> pin;
    attempts++;
   =====
   #distractorwhile(input == pin && attempts == 3);
   =====
   #distractorwhile(input != pin && attempts != 3);