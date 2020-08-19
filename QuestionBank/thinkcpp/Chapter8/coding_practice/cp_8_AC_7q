.. activecode:: cp_8_AC_7q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter8
   :subchapter: coding_practice
   :topics: Chapter8/coding_practice
   :from_source: T
   :language: cpp

   #include <iostream>
   using namespace std;

   struct Pokemon {
       string pokeName;
       string type;
       int level;
       int healthPercentage;
   };

   struct Trainer {
       // Write your implementation here.
   };

   void printPokeInfo(Pokemon p);

   void printTrainerInfo (Trainer t) {
       // Write your implementation here.
   }

   int main() {
       Pokemon pikachu = { "Pikachu", "Electric", 81, 100 };
       Pokemon espeon = { "Espeon", "Psychic", 72, 100 };
       Pokemon snorlax = { "Snorlax", "Normal", 75, 100 };
       Pokemon venusaur = { "Venusaur", "Grass & Poison", 77, 100 };
       Pokemon charizard = { "Charizard", "Fire & Flying", 77, 100 };
       Pokemon blastoise = { "Blastoise", "Water", 77, 100 };
       Trainer red = { "Red", 'M', 8, pikachu, espeon, snorlax, venusaur, charizard, blastoise };
       printTrainerInfo (red);
   }
   ====
   void printPokeInfo(Pokemon p) {
       cout << p.pokeName << " (Lv. " << p.level << ", " << p.healthPercentage << "% HP)" << endl;
   }