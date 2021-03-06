.. activecode:: lcfrhbb1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: ArrayBasics
   :subchapter: horseBarnB
   :topics: ArrayBasics/horseBarnB
   :from_source: T
   :language: java

   interface Horse
   {
      /** @return the horse's name */
      String getName();

      /** @return the horse's weight */
      int getWeight();
   }

   class Horsey implements Horse
   {
      private String name;
      private int weight;

      public Horsey(String theName, int theWeight)
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


      /** Consolidates the barn by moving horses so that the horses are
       *  in adjacent spaces, starting at index 0, with no empty space
       *  between any two horses.
       * Postcondition: The order of the horses is the same as before
       *  the consolidation.
       */
      public void consolidate()
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
        barn.spaces[0] = new Horsey("Trigger", 1340);
        barn.spaces[2] = new Horsey("Silver",1210);
        barn.spaces[5] = new Horsey("Patches", 1350);
        barn.spaces[6] = new Horsey("Duke", 1410);
        System.out.println("before consolidate");
        System.out.println(barn);
        barn.consolidate();
        System.out.println("after consolidate");
        System.out.println(barn);
      }
   }