.. mchoice:: qoom_4
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit9-Inheritance/ooMedMC
   :from_source: T
   :practice: T
   :answer_a: Meow Moo Woof Awk Awk
   :answer_b: Awk Awk Awk Awk Awk
   :answer_c: This will not compile
   :answer_d: This will have runtime errors
   :answer_e: Meow Moo Woof Oink Awk
   :correct: a
   :feedback_a: Objects keep a reference to the class that created them. So, even if you put them in an array of <code>Animal</code> objects, they know what they are and all methods are resolved starting with the class of the object. <code>Bird</code> and <code>Pig</code> do not override speak so the <code>speak</code> method in <code>Animal</code> will execute.
   :feedback_b: Methods are always resolved starting with the class of the object, so <code>Cat</code>, <code>Cow</code>, and <code>Dog</code> will all execute their overridden <code>speak</code> methods, so the output will be: Meow Moo Woof Awk Awk.
   :feedback_c: Because <code>Bird</code>, <code>Cow</code>, <code>Cat</code>, <code>Dog</code>, and <code>Pig</code> are subclasses of <code>Animal</code>, they can be stored in an array declared as <code>Animal</code> without any compile time errors.
   :feedback_d: Because <code>Bird</code>, <code>Cow</code>, <code>Cat</code>, <code>Dog</code>, and <code>Pig</code> are subclasses of <code>Animal</code>, they can be stored in an array declared as <code>Animal</code> without any runtime errors.
   :feedback_e: The <code>Pig</code> class did not override the <code>speak</code> method, so it will use the method from <code>Animal</code>, thus the output should be: Meow Moo Woof Awk Awk

    If you have a parent class ``Animal`` that has a method ``speak()`` which returns: Awk. ``Cat`` has a ``speak`` method that returns: Meow.  ``Bird`` does not have a ``speak`` method.  ``Dog`` has a ``speak`` method that returns: Woof.  ``Pig`` does not have a ``speak`` method.  ``Cow`` has a ``speak`` method that returns: Moo.   What is the output from looping through the array ``a`` created below and asking each element to ``speak()``?

    .. code-block:: java

          Animal[] a = { new Cat(), new Cow(), new Dog(), new Pig(), new Bird() }