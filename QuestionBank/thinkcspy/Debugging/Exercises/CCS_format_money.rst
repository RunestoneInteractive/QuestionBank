.. activecode:: CCS_format_money
   :author: Michael McCarrin
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Debugging
   :subchapter: Exercises
   :topics: Debugging/Exercises
   :from_source: F

   Add code to complete the program below. The finished program should:
   
   #. ask the user to enter a number of dollars between 0 and 1,000 and a number of pennies between 0 and 99,
   #. read in both values as ints,
   #. print a message displaying the total amount of money as a single number with two decimal places.
   
   **Examples:**
   
   * If the user enters 100 dollars and 50 cents, the output should read "$100.50"
   * If the user enters 1 dollar and 5 cents, the output should read "$1.05"
   * If the user enters 0 dollars and 99 cents, the output should read "$0.99"
      
   **NOTE: The IF statement is not permitted. Likewise, comparison operators are not permitted. You should do this using just the basic operators you have studied so far.**
   ~~~~
   dollars = int(input("Please enter a number of dollars between 0 and 1000:"))

   cents   = int(input("Please enter a number of cents between 0 and 99:"))

   # YOUR CODE HERE

   total   = "$0.00" # FIXME 

   print(total)