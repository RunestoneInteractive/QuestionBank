.. activecode:: LHSQuestionFourteen
    :author: Wesley Thang
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: Dictionaries
    :subchapter: Exercises
    :topics: Dictionaries/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 26.0

    Write a function called ``check_inventory(inventory, low)`` that returns a sorted list of items
    that are below an inventory level that is given by the ``low`` integer parameter. The function
    will work without the ``low`` parameter supplied - in which case, you should assume ``low`` is 5.
    
    Example: If the inventory is ``{ 'apple':10, 'banana':3 }``, ``check_inventory(inventory)`` 
    will return the list ``['banana']``
    
    ~~~~
        
    def check_inventory(inventory, low):
        # your code here
    
    def main():
        # your test code here
    
    if __name__ == "__main__":
        main()
        
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def _golden(self, inventory, low=5):
            buy = []
            for (item, quantity) in inventory.items():
                if quantity < low:
                    buy.append(item)
            buy.sort()
            return(buy)
    
        def testOne(self):
            SelfTest = False
            if (SelfTest):
                self.assertEqual(0,1,"Auto-testing if OFF - you must check program yourself for now")
                return
    
            print('Auto-testing...')
    
            i1 = {'apple':6 , 'watermelon':2, 'orange':10, 'pear':3, 'jackfruit':20 }
            tests = [ (i1, 10),
                      (i1, 11),
                      (i1, None)
                    ]
    
            num=0
            for t in tests:
                if t[1] == None:
                    self.assertEqual(check_inventory(t[0]), self._golden(t[0]), 'test case ' + str(num)  )
                else:
                    self.assertEqual(check_inventory(t[0], t[1]), self._golden(t[0], t[1]), 'test case ' + str(num)  )
                num += 1
    
    myTests().main()