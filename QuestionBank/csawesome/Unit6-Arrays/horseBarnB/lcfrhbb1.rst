.. activecode:: lcfrhbb1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: horseBarnB
   :topics: Unit6-Arrays/horseBarnB
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.4324324324
   :total_students_attempting: 37
   :num_students_correct: 30.0
   :mean_clicks_to_correct: 1.8333333333

   Try to write the code for the method ``consolidate`` in the ``HorseBarn`` class. When you are ready click "Run" to test your solution.
   ~~~~
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
        barn.spaces[0] = new Horse("Trigger", 1340);
        barn.spaces[2] = new Horse("Silver",1210);
        barn.spaces[5] = new Horse("Patches", 1350);
        barn.spaces[6] = new Horse("Duke", 1410);
        System.out.println("before consolidate");
        System.out.println(barn);
        barn.consolidate();
        System.out.println("after consolidate");
        System.out.println(barn);
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;
    import java.lang.reflect.Field;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "space 0 has name: Trigger weight: 1340\nspace 1 has name: Silver weight: 1210\nspace 2 has name: Patches weight: 1350\nspace 3 has name: Duke weight: 1410\nspace 4 has  null \nspace 5 has  null \nspace 6 has  null";
   
            boolean passed = removeSpaces(output).contains(removeSpaces(expect));
            getResults(expect, output, "Expected output from main", passed);
            assertTrue(passed);
        }
   
        @Test
        public void test1() {
            HorseBarn barn = new HorseBarn(7);
   
            try {
                Field barnField = HorseBarn.class.getDeclaredField("spaces");
                barnField.setAccessible(true);
   
                Horse[] spaces = (Horse[]) barnField.get(barn);
   
                spaces[1] = new Horse("Trigger", 1340);
                spaces[3] = new Horse("Silver",1210);
                spaces[5] = new Horse("Lady", 1575);
   
                String expect = "space 0 has name: Trigger weight: 1340\nspace 1 has name: Silver weight: 1210\nspace 2 has name: Lady weight: 1575\nspace 3 has  null \nspace 4 has  null \nspace 5 has  null \nspace 6 has  null";
                barn.consolidate();
                String actual = barn.toString();
   
                boolean passed = removeSpaces(actual).contains(removeSpaces(expect));
   
                String msg = "Checking consolidate() with [null, \"Trigger\", null, \"Silver\", null, \"Lady\", null, null]";
   
               getResults(expect, actual, msg, passed);
                assertTrue(passed);
   
            } catch (Exception e) {
                getResults("", "", "There was a error with the testing code.", false);
                fail();
            }
   
        }
    }