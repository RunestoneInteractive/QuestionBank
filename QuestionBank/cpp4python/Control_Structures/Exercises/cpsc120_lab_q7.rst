.. parsonsprob:: cpsc120_lab_q7
   :author: Matthew Zuniga
   :difficulty: 0.0
   :basecourse: cpp4python
   :chapter: Control_Structures
   :subchapter: Exercises
   :topics: Control_Structures/Exercises
   :from_source: F

   Sometimes, we unintentionally create <b>infinite loops.</b> An infinite loop occurs when a loop never reaches an exit condition. An <b>Alderson loop</b> (like Elliot Alderson from the hit TV series, Mr. Robot!) is when an exit condition is programmed but can never be reached.
   <br><br>
   This program is meant to sum numbers until it is greater than or equal to 100. Can you identify where and why this loop will go on infinitely?
   <br> <br>
   Construct a program that will fix this infinite loop. 
   <br> <br>
   The code is provided below. Assume all headers and namespace std is already at the top of the file.<br> <br>

   <code>bool sentinel = true;<br>
   int n = 0;<br>
   int sum = 0;<br>
   while(sentinel) { <br>
   &emsp;cout << "Enter a number: " << endl; <br>
   &emsp;cin >> n; <br>
   &emsp;n = 0; <br>
   &emsp;sum += n; <br>
   &emsp;if(sum >= 100) <br>
   &emsp;&emsp;sentinel=false;<br>
   &emsp;}<br>
   }<br><br>
   </code>
   -----
   bool sentinel = 0;
   int n = 0;
   int sum = 0;
   =====
   while(sentinel) {
    cout << "Enter a number: " << endl;
    cin >> n;
    sum += n;
   =====
    if(sum >= 100) { 
   =====
     sentinel = false;
     }
   =====
   }
   =====
   #distractorsentinel = true;
   }
   =====
   #distractorwhile(!sentinel) {
    cout << "Enter a number: " << endl;
    cin >> n;
    n = 0;
    sum += n;
   =====