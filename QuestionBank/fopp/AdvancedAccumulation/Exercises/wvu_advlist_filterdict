.. activecode:: wvu_advlist_filterdict
    :author: Brian Powell
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: AdvancedAccumulation
    :subchapter: Exercises
    :topics: AdvancedAccumulation/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.2571428571
    :total_students_attempting: 35
    :num_students_correct: 20.0
    :mean_clicks_to_correct: 2.2

    Use dictionary comprehension to filter the dictionary of total coal production. Your dictionary should only contain those counties that actually produced coal. Produce a dictionary named **coal_producers** where the key is the county name and value is the total production from that county. There are 37 counties that produced coal.
    
    ~~~~
    coal =  {'Barbour': 22698709, 'Berkeley': 0, 'Boone': 129299662, 'Braxton': 6148194, 'Brooke': 12640129, 'Cabell': 0, 'Calhoun': 0, 'Clay': 12105925, 'Doddridge': 0, 'Fayette': 78725415, 'Gilmer': 1524306, 'Grant': 10453350, 'Greenbrier': 9752538, 'Hampshire': 0, 'Hancock': 363000, 'Hardy': 0, 'Harrison': 53100021, 'Jackson': 0, 'Jefferson': 0, 'Kanawha': 97320148, 'Lewis': 2468571, 'Lincoln': 5240664, 'Logan': 145946946, 'Marion': 77960242, 'Marshall': 49287824, 'Mason': 2399022, 'McDowell': 154968249, 'Mercer': 18179446, 'Mineral': 3500919, 'Mingo': 88518551, 'Monongalia': 100091243, 'Monroe': 0, 'Morgan': 0, 'Nicholas': 38266879, 'Ohio': 12652255, 'Pendleton': 0, 'Pleasants': 0, 'Pocahontas': 501600, 'Preston': 21247972, 'Putnam': 2073603, 'Raleigh': 102644769, 'Randolph': 9552926, 'Ritchie': 0, 'Roane': 0, 'Summers': 51458, 'Taylor': 4267413, 'Tucker': 8327096, 'Tyler': 0, 'Upshur': 12462267, 'Wayne': 14007294, 'Webster': 15423668, 'Wetzel': 0, 'Wirt': 0, 'Wood': 0, 'Wyoming': 69590753}
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertEqual(len(coal_producers),37,"37 counties produced coal.")
            self.assertEqual("Berkeley" in coal_producers,False,"Berkeley County produced no coal")
            self.assertEqual("Boone" in coal_producers,True,"Boone County produced coal")
    
    myTests().main()