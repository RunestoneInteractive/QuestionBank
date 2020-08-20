.. activecode:: lcfrhba1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: horseBarnA
   :topics: Unit6-Arrays/horseBarnA
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.3333333333
   :total_students_attempting: 60
   :num_students_correct: 56.0
   :mean_clicks_to_correct: 3.4642857143

   FRQ HorseBarn A: Write the method findHorseSpace.
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
            String expect = "Index of Trigger should be 0 and is 0\nIndex of Silver should be 2 and is 2\nIndex of Coco should be -1 and is -1";
   
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
                spaces[4] = new Horse("Lady", 1575);
                spaces[6] = new Horse("Patches", 1350);
                spaces[0] = new Horse("Duke", 1410);
   
                String expected = "3";
                String actual = "" + barn.findHorseSpace("Silver");
   
                String msg = "Checking findHorseSpace(\"Silver\") with [\"Duke\", \"Trigger\", null, \"Silver\", \"Lady\", null, \"Patches\"]";
                boolean passed = getResults(expected, actual, msg);
                assertTrue(passed);
   
            } catch (Exception e) {
                getResults("", "", "There was a error with the testing code.", false);
                fail();
            }
   
        }
   
        @Test
        public void test2() {
            HorseBarn barn = new HorseBarn(7);
   
            try {
                Field barnField = HorseBarn.class.getDeclaredField("spaces");
                barnField.setAccessible(true);
   
                Horse[] spaces = (Horse[]) barnField.get(barn);
   
                spaces[1] = new Horse("Trigger", 1340);
                spaces[3] = new Horse("Silver",1210);
                //spaces[4] = new Horse("Lady", 1575);
                spaces[6] = new Horse("Patches", 1350);
                spaces[0] = new Horse("Duke", 1410);
   
                String expected = "-1";
                String actual = "" + barn.findHorseSpace("Lady");
   
                String msg = "Checking findHorseSpace(\"Lady\") with [\"Duke\", \"Trigger\", null, \"Silver\", null, null, \"Patches\"]";
                boolean passed = getResults(expected, actual, msg);
                assertTrue(passed);
   
            } catch (Exception e) {
                getResults("", "", "There was a error with the testing code.", false);
                fail();
            }
   
        }
    }