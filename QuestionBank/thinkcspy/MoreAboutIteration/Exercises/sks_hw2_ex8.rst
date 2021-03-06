.. activecode:: sks_hw2_ex8
    :author: Shishir Shah
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: Exercises
    :topics: MoreAboutIteration/Exercises
    :from_source: F
    :language: python
    :pct_on_first: 0.0
    :total_students_attempting: 10
    :num_students_correct: 5.0
    :mean_clicks_to_correct: 16.2

    Write a function ``drugPotency(loss, expire)`` that determines how many months a drug
    can remain in storage given a potency loss percentage (``loss``) and an expiration
    target (``expire``). For example, if a certain drug looses 4% of its effectiveness
    every month it is in storage, and when its effectiveness is below 50% it is considered 
    expired and must be discarded, then the function should compute the number of months 
    it would be when the drug expires and should be discarded. The function should print the 
    effectiveness for each month that the drug is in storage. 
    
    As an example, the output from ``drugPotency(4.0, 50.0)`` would be::
    
        Month: 0    effectiveness: 100.0
        Month: 1    effectiveness: 96.0
        Month: 2    effectiveness: 92.16
        Month: 3    effectiveness: 88.4736
        Month: 4    effectiveness: 84.934656
        Month: 5    effectiveness: 81.53726976
        Month: 6    effectiveness: 78.2757789696
        Month: 7    effectiveness: 75.1447478108
        Month: 8    effectiveness: 72.1389578984
        Month: 9    effectiveness: 69.2533995824
        Month: 10   effectiveness: 66.4832635992
        Month: 11   effectiveness: 63.8239330552
        Month: 12   effectiveness: 61.270975733
        Month: 13   effectiveness: 58.8201367037
        Month: 14   effectiveness: 56.4673312355
        Month: 15   effectiveness: 54.2086379861
        Month: 16   effectiveness: 52.0402924666
        Month: 17   effectiveness: 49.958680768 DISCARDED
    
    
    ~~~~
    def drugPotency(loss, expire):
        # your code here
        
        
    def main():
        drugPotency(4.0, 50.0)
    
    if __name__ == "__main__":
        main()
        
    ====