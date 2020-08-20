.. activecode:: wvu_list_slice
   :author: Brian Powell
   :difficulty: 0.0
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: Exercises
   :topics: Sequences/Exercises
   :from_source: F
   :pct_on_first: 0.2625698324
   :total_students_attempting: 179
   :num_students_correct: 123.0
   :mean_clicks_to_correct: 2.7073170732

   We want to use the slicing operator to create a list named recent_presidents containing the presidents elected starting with the 32nd president, Franklin D. Roosevelt.
   ~~~~
   presidents = ['George Washington', 'John Adams', 'Thomas Jefferson','James Madison','James Monroe','John Quincy Adams','Andrew Jackson','Martin Van Buren','William Henry Harrison','John Tyler','James K. Polk', 'Zachary Taylor','Millard Fillmore','Franklin Pierce','James Buchanan','Abraham Lincoln','Andrew Johnson','Ulysses S. Grant','Rutherford B. Hayes','James A. Garfield','Chester A. Arthur','Grover Cleveland','Benjamin Harrison','Grover Cleveland','William McKinley','Theodore Roosevelt','William Howard Taft','Woodrow Wilson','Warren G. Harding','Calvin Coolidge','Herbert Hoover','Franklin D. Roosevelt','Harry S. Truman','Dwight D. Eisenhower','John F. Kennedy','Lyndon B. Johnson','Richard Nixon','Gerald Ford','Jimmy Carter','Ronald Reagan','George H.W. Bush','Bill Clinton','George W. Bush','Barack Obama','Donald Trump']
   
   # # Create a list named recent_presidents containing the 32nd through the most recent president
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(recent_presidents,presidents[31:],"Your recent_presidents list should contain Franklin D. Roosevelt through Donald Trump")
   
   myTests().main()