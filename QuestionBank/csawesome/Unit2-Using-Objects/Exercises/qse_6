.. mchoice:: qse_6
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: Exercises
   :topics: Unit2-Using-Objects/Exercises
   :from_source: T
   :practice: T
   :answer_a: 100.00
   :answer_b: 110.00
   :answer_c: 90.00
   :answer_d: 10.00
   :correct: b
   :feedback_a: Remember that we have added and withdrawn money
   :feedback_b: The constructor sets the total to 100, the withdraw method subtracts 30, and then the deposit method adds 40.
   :feedback_c: We added more money than we took out
   :feedback_d: We set the value of total to be 100 first
   :pct_on_first: 0.7335526316
   :total_students_attempting: 1824
   :num_students_correct: 1810.0
   :mean_clicks_to_correct: 1.4325966851

   Given the BankAccount class definition below, what is the output of the code in the main method?
   
   .. code-block:: java
   
    public class BankAccount
    {
        private int accountID;
        private double total;
   
        public BankAccount(int id, double initialDeposit)
        {
            accountID = id;
            total = initialDeposit;
        }
   
        public void deposit(double money)
        {
            total = total + money;
        }
   
        public void withdraw(double money)
        {
            total = total - money;
        }
   
        public void printCurrentTotal()
        {
            System.out.print(total);
        }
   
        public static void main(String[] args)
        {
            BankAccount newAccount = new BankAccount(12345, 100.00);
            newAccount.withdraw(30.00);
            newAccount.deposit(40.00);
            newAccount.printCurrentTotal();
        }
    }