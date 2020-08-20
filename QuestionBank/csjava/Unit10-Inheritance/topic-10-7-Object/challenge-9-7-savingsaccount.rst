.. activecode:: challenge-9-7-savingsaccount
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit10-Inheritance
   :subchapter: topic-10-7-Object
   :topics: Unit10-Inheritance/topic-10-7-Object
   :from_source: T
   :language: java

   Complete the subclass SavingsAccount below which inherits from Account and adds an interest rate variable. Write a toSTring and an equals method for it.
   ~~~~
   public class Account
   {
       private String name;
       private double balance;

       public Account(String name, double balance)
       {
          this.name = name;
          this.balance = balance;
       }
       public static void main(String[] args)
       {

       }
   }

   class SavingsAccount
   {

   }