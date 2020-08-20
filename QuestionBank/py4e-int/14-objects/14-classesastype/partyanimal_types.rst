.. activecode:: partyanimal_types
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 14-objects
   :subchapter: 14-classesastype
   :topics: 14-objects/14-classesastype
   :from_source: T
   :coach:

   class PartyAnimal:
      x = 0

      def party(self) :
         self.x = self.x + 1
         print("So far",self.x)

   an = PartyAnimal()
   print ("Type", type(an))
   print ("Dir ", dir(an))
   print ("Type", type(an.x))
   print ("Type", type(an.party))