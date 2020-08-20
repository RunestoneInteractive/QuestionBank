.. activecode:: animals_js_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: JS4Python
    :chapter: ObjectOriented
    :subchapter: inheritance
    :topics: ObjectOriented/inheritance
    :from_source: T
    :language: javascript

    "use strict"
    class Animal {
        constructor(name) {
            this._name = name
        }

        speak() {
            writeln("Generic animals are Mute")
        }

        get name() {
            return this._name;
        }
    }

    class Dog extends Animal {

        constructor(name) {
            super(name);
            this.numLegs = 4;
        }

        speak() {
            writeln("woof woof");
        }
    }

    class CartoonDog extends Dog {

        speak() {
            writeln("I'll have a dry martini")
        }

    }

    var spot = new Dog('spot');
    spot.speak();
    writeln(spot.numLegs);
    brian = new CartoonDog('Brian')
    brian.speak()
    writeln(brian.name)