.. parsonsprob:: mucp_8_8
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter8
   :subchapter: mixed_up_code
   :topics: Chapter8/mixed_up_code
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Let's write the code for the ``printAddress`` function. ``printAddress`` takes
   an ``Employee`` as a parameter and should print out the information of the employee in the
   following format: name (id) lives at houseNumber in state, postalAddress.
   Put the necessary blocks of code in the correct order.
   -----
   void printAddress (Employee e) {
   =====
   string printAddress (Employee& e) {  #paired
   =====
      cout << e.name << " (" << e.id << ") lives at ";
   =====
      cout << e.address.name << " (" << e.address.id << ") lives at ";  #distractor
   =====
      cout << e.name << "(" << e.address.id << ") lives at";  #distractor
   =====
      cout << e.address.houseNumber << " in " << e.address.state << ", " << e.address.postalAddress << endl;
   =====
      cout << e.houseNumber << " in " << e.state << ", " << e.postalAddress << endl;  #distractor
   =====
   }