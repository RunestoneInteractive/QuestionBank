.. mchoice:: setSignature
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit6-Writing-Classes
    :subchapter: topic-6-5-mutator-methods
    :topics: Unit6-Writing-Classes/topic-6-5-mutator-methods
    :from_source: F
    :practice: T

    Consider the class Party which keeps track of the number of people at the party.

    .. code-block:: java

        public class Party
        {
            //number of people at the party
            private int numOfPeople;

            /* Missing header of set method */
            {
                numOfPeople = people;
            }
        }

    Which of the following method signatures could replace the missing header for the set method in the code above so that the method will work as intended?

    - public int getNum(int people)

      - The set method should not have a return value and is usually named set, not get.

    - public int setNum()

      - The set method should not have a return value and needs a parameter.

    - public int setNum(int people)

      - The set method should not have a return value.

    - public void setNum(int people)

      + Yes, the set method should take a parameter called people and have a void return value. The name of the set method is usually set followed by the full instance variable name, but it does not have to be an exact match.

    - public int setNumOfPeople(int p)

      - The parameter of this set method should be called people in order to match the code in the method body.