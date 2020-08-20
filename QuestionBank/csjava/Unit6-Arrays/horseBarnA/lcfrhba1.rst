.. activecode:: lcfrhba1
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit6-Arrays/horseBarnA
   :from_source: T
   :language: java

   class Horse
   {
      private String name;
      private int weight;

      public Horse(String theName, int theWeight)
      {
         this.name = theName;
         this.weight = theWeight;
      }

      public String getName() { return this.name;}

      public int getWeight() { return this.weight; }

      public String toString()
      {
         return "name: " + this.name + " weight: " + this.weight;
      }
   }


   public class HorseBarn
   {
      private Horse[] spaces;

      /** Constructor that takes the number of stalls
       * @param numStalls - the number of stalls in the barn
       */
      public HorseBarn(int numStalls)
      {
        spaces = new Horse[numStalls];
      }

      /** Returns the index of the space that contains the horse with the specified name.
       * * Precondition: No two horses in the barn have the same name.
       * @param name the name of the horse to find
       * @return the index of the space containing the horse with the specified name;
       * -1 if no horse with the specified name is in the barn.
       */
      public int findHorseSpace(String name)
      {

      }

      public String toString()
      {
        String result = "";
        Horse h = null;
        for (int i = 0; i < spaces.length; i++) {
          h = spaces[i];
          result = result + "space " + i + " has ";
          if (h == null) result = result + " null \n";
          else result = result + h.toString() + "\n";
        }
        return result;
      }

      public static void main (String[] args)
      {
        HorseBarn barn = new HorseBarn(7);
        barn.spaces[0] = new Horse("Trigger", 1340);
        barn.spaces[2] = new Horse("Silver",1210);
        barn.spaces[3] = new Horse("Lady", 1575);
        barn.spaces[5] = new Horse("Patches", 1350);
        barn.spaces[6] = new Horse("Duke", 1410);

        // print out what is in the barn
        System.out.println(barn);

        // test
        System.out.println("Index of Trigger should be 0 and is " +
                           barn.findHorseSpace("Trigger"));
        System.out.println("Index of Silver should be 2 and is " +
                           barn.findHorseSpace("Silver"));
        System.out.println("Index of Coco should be -1 and is " +
                           barn.findHorseSpace("Coco"));
      }
   }