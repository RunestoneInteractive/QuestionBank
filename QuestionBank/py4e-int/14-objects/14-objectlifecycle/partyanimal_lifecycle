.. activecode:: partyanimal_lifecycle
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 14-objects
   :subchapter: 14-objectlifecycle
   :topics: 14-objects/14-objectlifecycle
   :from_source: T
   :coach:

   class PartyAnimal:
      x = 0

      def __init__(self):
         print('I am constructed')

      def party(self) :
         self.x = self.x + 1
         print('So far',self.x)

      def __del__(self):
         print('I am destructed', self.x)

   an = PartyAnimal()
   an.party()
   an.party()
   an = 42
   print('an contains',an)