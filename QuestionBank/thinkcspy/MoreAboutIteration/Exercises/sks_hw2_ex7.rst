.. activecode:: sks_hw2_ex7
    :author: Shishir Shah
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: Exercises
    :topics: MoreAboutIteration/Exercises
    :from_source: F
    :language: python
    :pct_on_first: 0.125
    :total_students_attempting: 8
    :num_students_correct: 6.0
    :mean_clicks_to_correct: 14.6666666667

    Say that you owe the credit card company $1000.00. The company charges you 1.5% per month 
    on the unpaid balance. You have decided to stop using the card and pay off the debt by making a 
    monthly payment of ``N`` dollars a month. Write a function that takes the monthly interest rate, the starting 
    balance and the monthy payment as parameters, then writes out the balance and total payments for 
    every month until the balance is zero or less. Also, when the balance falls below the amount of the 
    monthly payment, write out the final payment that will bring the balance to exactly zero. 
    
    A sample output for monthly interest rate of 1.5%, starting balance of $1000, and monthly payment of 
    $100 would look like:
    
    ::
    
      Month: 1 	balance: 915.0 	total payments: 100.0
      Month: 2 	balance: 828.725 	total payments: 200.0
      Month: 3 	balance: 741.155875 	total payments: 300.0
      Month: 4 	balance: 652.273213125 	total payments: 400.0
      Month: 5 	balance: 562.057311322 	total payments: 500.0
      Month: 6 	balance: 470.488170992 	total payments: 600.0
      Month: 7 	balance: 377.545493557 	total payments: 700.0
      Month: 8 	balance: 283.20867596 	total payments: 800.0
      Month: 9 	balance: 187.456806099 	total payments: 900.0
      Month: 10 	balance: 90.2686581908 	total payments: 1000.0
      Month: 11 	balance: 0 	total payments: 1091.62268806
    
    
    ~~~~
    
    def creditCardBill(rate, balance, payment):
        # your code here
    
    def main():
        creditCardBill(1.5, 1000.0, 100.0)
    
    if __name__ == "__main__":
        main()
        
    ====