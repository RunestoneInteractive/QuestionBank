.. mchoice:: qtnt5_17
    :author: bmiller
    :difficulty: 3.0
    :basecourse: apcsareview
    :chapter: Tests
    :subchapter: test5nt
    :topics: Tests/test5nt
    :from_source: T
    :answer_a: run eat
    :answer_b: run eat sleep
    :answer_c: run eat sleep bark
    :answer_d: run eat bark sleep
    :answer_e: Nothing is printed due to infinite recursion
    :correct: d
    :feedback_a: Because the fido is an "Underdog", we will call the eat() from class Underdog, http://tinyurl.com/AP19-Q25
    :feedback_b: Because the fido is an "Underdog", we will call the eat() from class Underdog, http://tinyurl.com/AP19-Q25
    :feedback_c: Because the fido is an "Underdog", we will call the eat() from class Underdog, http://tinyurl.com/AP19-Q25
    :feedback_d: Because the fido is an "Underdog", we will call the eat() from class Underdog, http://tinyurl.com/AP19-Q25
    :feedback_e: Because the fido is an "Underdog", we will call the eat() from class Underdog, http://tinyurl.com/AP19-Q25

    Consider the following code. What is printed?

    .. code-block:: java

        class Dog{

          public void act(){
              System.out.print("run ");
              eat();
          }
          public void eat(){
              System.out.print("eat ");
          }
        }

        public class UnderDog extends Dog{

          public void act(){
              super.act();
              System.out.print("bark ");
          }

          public void eat(){
              super.eat();
              System.out.print("bark ");
          }

          public static void main(String[] args){
              Dog fido = new UnderDog();
              fido.act();
          }
        }