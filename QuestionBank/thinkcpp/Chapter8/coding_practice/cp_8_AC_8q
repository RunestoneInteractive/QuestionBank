.. activecode:: cp_8_AC_8q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter8
    :subchapter: coding_practice
    :topics: Chapter8/coding_practice
    :from_source: T
    :language: cpp

    When Pokemon are injured, they can be healed up at the Pokemon Center.
    Write the function ``healPokemon``, which takes a ``Trainer`` as a parameter
    and heals the Trainer's Pokemon to 100 percent health.
    ~~~~
    #include <iostream>
    using namespace std;

    struct Pokemon {
        string pokeName;
        string type;
        int level;
        int healthPercentage;
    };

    struct Trainer {
        string trainerName;
        char gender;
        int numBadges;
        Pokemon first, second, third, fourth, fifth, sixth;
    };

    void printPokeInfo(Pokemon p);
    void printTrainerInfo(Trainer t);

    void healPokemon(Trainer& t) {
        // Write your implementation here.
    }

    int main() {
        Pokemon exeggutor = {"Exeggutor", "Grass & Psychic", 58, 78};
        Pokemon alakazam = {"Alakazam", "Psychic", 54, 0};
        Pokemon arcanine = {"Arcanine", "Fire", 58, 24};
        Pokemon rhydon = {"Rhydon", "Ground & Rock", 56, 55};
        Pokemon gyarados = {"Gyarados", "Water & Flying", 58, 100};
        Pokemon pidgeot = {"Pidgeot", "Normal & Flying", 56, 35};
        Trainer blue = {"Blue", 'M', 8, exeggutor, alakazam, arcanine, rhydon, gyarados, pidgeot};
        printTrainerInfo(blue);
        healPokemon(blue);
        printTrainerInfo(blue);  // Pokemon should now all be healed to 100% health
    }
    ====
    void printPokeInfo(Pokemon p) {
        cout << p.pokeName << " (Lv. " << p.level << ", " << p.healthPercentage << "% HP)" << endl;
    }

    void printTrainerInfo(Trainer t) {
        cout << "Trainer " << t.trainerName << " has " << t.numBadges
            << " badges and " << t.trainerName << "'s team consists of " << endl;
        printPokeInfo(t.first);
        printPokeInfo(t.second);
        printPokeInfo(t.third);
        printPokeInfo(t.fourth);
        printPokeInfo(t.fifth);
        printPokeInfo(t.sixth);
    }