.. activecode:: wvu_list_count
   :author: Brian Powell
   :difficulty: 1.0437787185
   :basecourse: fopp
   :chapter: Sequences
   :subchapter: Exercises
   :topics: Sequences/Exercises
   :from_source: F
   :pct_on_first: 0.4227642276
   :total_students_attempting: 123
   :num_students_correct: 74.0
   :mean_clicks_to_correct: 1.7432432432

   We want to see how many times Grover Cleveland was president. Store the result in a variable named grover_count.
   ~~~~
   presidents = ['George Washington', 'John Adams', 'Thomas Jefferson','James Madison','James Monroe','John Quincy Adams','Andrew Jackson','Martin Van Buren','William Henry Harrison','John Tyler','James K. Polk', 'Zachary Taylor','Millard Fillmore','Franklin Pierce','James Buchanan','Abraham Lincoln','Andrew Johnson','Ulysses S. Grant','Rutherford B. Hayes','James A. Garfield','Chester A. Arthur','Grover Cleveland','Benjamin Harrison','Grover Cleveland','William McKinley','Theodore Roosevelt','William Howard Taft','Woodrow Wilson','Warren G. Harding','Calvin Coolidge','Herbert Hoover','Franklin D. Roosevelt','Harry S. Truman','Dwight D. Eisenhower','John F. Kennedy','Lyndon B. Johnson','Richard Nixon','Gerald Ford','Jimmy Carter','Ronald Reagan','George H.W. Bush','Bill Clinton','George W. Bush','Barack Obama','Donald Trump']
   
   # Store the number of times Grover Cleveland was president in grover_count
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(grover_count,presidents.count("Grover Cleveland"),"You didn't count the number of times correctly.")
   
   myTests().main()