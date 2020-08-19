.. activecode:: challenge-9-7-savingsaccount
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: topic-9-7-Object
   :topics: Unit9-Inheritance/topic-9-7-Object
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.5
   :total_students_attempting: 2
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Complete the subclass SavingsAccount below which inherits from Account and adds an interest rate variable. Write a constructor with 3 arguments, a toString, and an equals method for it. Uncomment the code in main to test your new class and methods.
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
   
       public String toString() {
        return name + ", " + balance;
       }
   
       public boolean equals(Object other)
       {
          Account otherAccount = (Account) other;
          return (this.balance == otherAccount.balance) &&
                        this.name.equals(otherAccount.name);
       }
   
       public static void main(String[] args)
       {
           Account acct1 = new Account("Armani Smith",1500);
                   System.out.println(acct1);
           // Uncomment this code to test SavingsAccount
           /*
           SavingsAccount acct2 = SavingsAccount("Dakota Jones",1500,4.5);
           SavingsAccount acct3 = SavingsAccount("Dakota Jones",1500,4.5);
                   System.out.println(acct2);
                   System.out.println(acct2.equals(acct3));
           */
       }
   }
   /* Write the SavingsAccount class which inherits from Account
      and has an interest rate and a constructor, toString, and
      equals methods.
   */
   class SavingsAccount
   {
   
   }
   ====
   import static org.junit.Assert.*;
     import org.junit.*;;
     import java.io.*;
   
     public class RunestoneTests extends CodeTestHelper
     {
         public RunestoneTests() {
             super("Account");
         }
   
         @Test
         public void test1()
         {
             String output = getMethodOutput("main");
             String expect = "Armani Smith, 1500.0\nDakota Jones, 1500.0, 4.5\ntrue";
   
             boolean passed = getResults(expect, output, "Checking output from main()");
             assertTrue(passed);
         }
   
         @Test
         public void test3()
         {
             String target = "public String toString()";
   
             String code = getCode();
             int index = code.indexOf("class SavingsAccount");
             code = code.substring(index);
             boolean passed = code.contains(target);
   
             getResults("true", ""+passed, "Checking that code contains toString() in SavingsAccount", passed);
             assertTrue(passed);
         }
   
         @Test
         public void test30()
         {
             String target = "super.toString()";
   
             String code = getCode();
             int index = code.indexOf("class SavingsAccount");
             code = code.substring(index);
   
             boolean passed = code.contains(target);
   
             getResults("true", ""+passed, "Checking that code contains call to super.toString() in SavingsAccount", passed);
             assertTrue(passed);
         }
         @Test
         public void containsExtends()
             {
                String target = "SavingsAccount extends Account";
                boolean passed = checkCodeContains(target);
                assertTrue(passed);
             }
   
         @Test
         public void test31()
         {
             String target = "public boolean equals(Object other)";
   
             String code = getCode();
             int index = code.indexOf("class SavingsAccount");
             code = code.substring(index);
   
             boolean passed = code.contains(target);
   
             getResults("true", ""+passed, "Checking that code contains equals() in SavingsAccount", passed);
             assertTrue(passed);
         }
   
         @Test
         public void test32()
         {
             String target = "super.equals(";
   
             String code = getCode();
             int index = code.indexOf("class SavingsAccount");
             code = code.substring(index);
   
             boolean passed = code.contains(target);
   
             getResults("true", ""+passed, "Checking that code contains call to super.equals() in SavingsAccount", passed);
             assertTrue(passed);
   
         }
     }