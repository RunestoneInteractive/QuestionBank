.. activecode:: json_class
    :author: bmiller
    :difficulty: 3.0
    :basecourse: webfundamentals
    :chapter: Dynamic
    :subchapter: localstorage
    :topics: Dynamic/localstorage
    :from_source: T
    :language: javascript

    class Item {
        constructor(name, quantity, priority, store, section, price) {
            this.name = name;
            this.quantity = quantity;
            this.priority = priority;
            this.store = store;
            this.section = section;
            this.price = price;

            this._purchased = false;
        }

        plainMethod() {
            alert("hello from a plain method");
        }

        get purchased() {
            return this._purchased;
        }

        set purchased(nv) {
            this._purchased = nv;
            alert(`${this.name} was purchased`)
        }

    }

    x = new Item('bread', 1, 'High', 'Fareway', 'Bakery', 3.99);
    writeln(x.constructor.name)

    y = JSON.stringify(x)
    writeln(y)

    z = JSON.parse(y)
    writeln(z)
    writeln(z.constructor.name)
    z.purchased = 10  // Note no alert!
    z.plainMethod() // Error!!