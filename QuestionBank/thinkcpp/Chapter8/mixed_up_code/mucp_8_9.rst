.. parsonsprob:: mucp_8_9
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter8
   :subchapter: mixed_up_code
   :topics: Chapter8/mixed_up_code
   :from_source: T
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 8.0

   Sometimes employees will move around and thus we'll need to update their addresses.
   Let's write the code for the ``updateAddress`` function. ``updateAddress`` takes an
   ``Employee`` and a new ``Address`` as parameters and sets the employee's address to the new address.
   Put the necessary blocks of code in the correct order.
   -----
   void updateAddress (Employee& e, Address a) {
   =====
   void updateAddress (Employee e, Address& a) {  #distractor
   =====
   void updateAddress (Employee e, Address a) {  #distractor
   =====
   Employee updateAddress (Employee e, Address a) {  #distractor
   =====
      e.address = a;
   =====
      e.address = address;  #distractor
   =====
      e.address.houseNumber = a.houseNumber;  #distractor
   =====
      e.address.state = a.state;  #distractor
   =====
      e.address.houseNumber = a.houseNumber;  #distractor
   =====
      e.address.postalAddress = a.postalAddress;  #distractor
   =====
   }
   =====
   };  #distractor