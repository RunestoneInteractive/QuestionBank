.. activecode:: partyanimal
  :author: bmiller
  :difficulty: 3.0
  :basecourse: py4e-int
  :chapter: 14-objects
  :subchapter: 14-ourfirstpythonobject
  :topics: 14-objects/14-ourfirstpythonobject
  :from_source: T
  :coach:

  class PartyAnimal:
      x = 0

      def party(self) :
         self.x = self.x + 1
         print("So far",self.x)

  an = PartyAnimal()
  an.party()
  an.party()
  an.party()
  PartyAnimal.party(an)