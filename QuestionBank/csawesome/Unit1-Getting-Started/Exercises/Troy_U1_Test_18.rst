.. activecode:: Troy_U1_Test_18
   :author: Shawn Haarer
   :difficulty: 1.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: Exercises
   :topics: Unit1-Getting-Started/Exercises
   :from_source: F
   :language: java

   Write a program that will calculate the cost of buying five items at 
   $16.95 each.  
   It will also calculate the sales tax at rate of 8% and add it to the 
   subtotal.  
   You will then need to display your output in a sentence or two, such as:  

   "You purchased 5 items at $16.95 each.
   The total cost, with tax, will be xxxxx   


   Your print statements must use variables for the following 
      - number of items,  

      - price, 

      - total cost

   You may also want variables for the 
     - tax rate,  

     - subtotal (the cost before tax), 
   
     - dollar amount of tax.  



   After you get this program to work, change the price to $10.99 and the 
   number of items to 4 
   and run it again, making sure that it still works properly.  

   Bonus - make the TAXRATE a constant or a final.  
   

   Recommendaton:  Compile your program after every line or two you 
   code.  
   It should make it much easier to fix compile time errors. 
   
   ~~~~

   public class Sales_Tax
   {
    public static void main (String [] args) 
    {
        System.out.println("Welcome to the Sales Tax program"); 

        // your code here 
        


        System.out.println("That completes the sales tax program");  
    }
}