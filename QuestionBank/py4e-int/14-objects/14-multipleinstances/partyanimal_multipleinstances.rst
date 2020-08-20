.. codelens:: partyanimal_multipleinstances
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 14-objects
   :subchapter: 14-multipleinstances
   :topics: 14-objects/14-multipleinstances
   :from_source: T
   :showoutput:

   class PartyAnimal:
      x = 0
      name = ''

      def __init__(self, nam):
         self.name = nam
         print(self.name,'constructed')

      def party(self) :
         self.x = self.x + 1
         print(self.name,'party count',self.x)

   s = PartyAnimal('Sally')
   j = PartyAnimal('Jim')

   s.party()
   j.party()
   s.party()