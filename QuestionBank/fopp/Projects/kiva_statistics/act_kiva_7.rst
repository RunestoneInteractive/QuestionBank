.. activecode:: act_kiva_7
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Projects
    :subchapter: kiva_statistics
    :topics: Projects/kiva_statistics
    :from_source: T
    :include: act_kiva_1
    :pct_on_first: 0.2848101266
    :total_students_attempting: 790
    :num_students_correct: 620.0
    :mean_clicks_to_correct: 4.6

    For each unique country name, print a line that shows the name of the country and then the number of loans made in that country, like this: "Guatemala 1"
    ~~~~
    unique_countries = ['Guatemala', 'Paraguay', 'Tajikistan', 'Kenya', 'Azerbaijan', 'El Salvador', 'Bolivia', 'Ecuador', 'Georgia', 'Philippines', 'Uganda', 'Madagascar', 'Nicaragua', 'Jordan']
    
    # Your code here
    ====
    from unittest.gui import TestCaseGui
    
    class MyTests(TestCaseGui):
    
        def testOne(self):
            res = '''Guatemala 1\nParaguay 2\nTajikistan 1\nKenya 3\nAzerbaijan 1\nEl Salvador 2\nBolivia 2\nEcuador 1\nGeorgia 1\nPhilippines 7\nUganda 1\nMadagascar 1\nNicaragua 1\nJordan 1\n'''
            self.assertEqual(self.getOutput(), res, "Use the accumulator pattern to add up all the loans")
    
    
    MyTests().main()