.. parsonsprob:: another_example_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter11
   :subchapter: another_example
   :topics: Chapter11/another_example
   :from_source: T
   :numbered: left
   :adaptive:

   Create the ``Cat`` object with member functions ``make_noise`` and ``catch_mouse``.
   The ``make_noise`` function should print different noises depending on the cat's mood.
   The ``catch_mouse`` function returns true if the product of the cat's weight and age is
   less than twice the speed of the mouse.  Write the functions in the same order they appear
   inside the structure. Use implicit variable access.
   -----
   struct Cat {
   =====
    int age, weight;
    string mood;
   =====
    void make_noise();
    bool catch_mouse(int speed);
   =====
   };
   =====
   void Cat::make_noise() {
   =====
    Cat cat = *this;                         #distractor
   =====
    if (mood == "happy") {
      cout << "purrr" << endl;
    }
    else {
      cout << "MEOW" << endl;
    }
   =====
    if (cat.mood == "happy") {                         #paired
     cout << "purrr" << endl;
    }
    else {
      cout << "MEOW" << endl;
    }
   =====
   }
   =====
    Cat cat = *this;                         #distractor
   =====
   bool Cat::catch_mouse(int speed) {
   =====
    if (speed * 2 > age * weight) {
      return true;
    }
    return false;
   }
   =====
    if (cat.speed * 2 > age * weight) {                          #paired
      return true;
    }
    return false;
   }
   =====
    if (speed * 2 < age * weight) {                         #distractor
      return true;
    }
    return false;
   }