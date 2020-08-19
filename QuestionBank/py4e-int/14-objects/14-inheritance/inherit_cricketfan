.. activecode:: inherit_cricketfan
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 14-objects
    :subchapter: 14-inheritance
    :topics: 14-objects/14-inheritance
    :from_source: T
    :language: python3
    :available_files: party.py

    from party import PartyAnimal

    class CricketFan(PartyAnimal):
      points = 0
      def six(self):
         self.points = self.points + 6
         self.party()
         print(self.name,"points",self.points)

    s = PartyAnimal("Sally")
    s.party()
    j = CricketFan("Jim")
    j.party()
    j.six()
    print(dir(j))