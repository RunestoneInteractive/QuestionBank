.. parsonsprob:: initialize_or_construct_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter11
   :subchapter: initialize_or_construct
   :topics: Chapter11/initialize_or_construct
   :from_source: T
   :numbered: left
   :adaptive:

   Implement two constructors for the ``Dog`` structure. One should be a default constructor, the other should take
   arguments. The weight needs to be converted from pounds to kilograms in the second constructor (for
   reference, 1 kilogram is approximately 2.2 pounds).
   -----
   struct Dog {
   =====
    int age, weight;
    string breed;
   =====
    Dog();
    Dog(int age_in, int weight_in, string breed_in);
   =====
   };
   =====
   Dog::Dog() {
   =====
    breed = "mutt";
    age = 1;
    weight = 18;
   =====
   }
   =====
   Dog::Dog(int age_in, int weight_in, string breed_in) {
   =====
    breed = breed_in;
    age = age_in;
   =====
    weight = weight_in / 2.2;
   }
   =====
    weight = weight_in * 2.2;                         #paired
   }