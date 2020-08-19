.. activecode:: time_part_a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit6-Writing-Classes
   :subchapter: timeFRQ
   :topics: Unit6-Writing-Classes/timeFRQ
   :from_source: T
   :language: java
   :autograde: unittest

   /**
    * Objects of the Time class hold a time value for
    * a European-style 24 hour clock.
    * The value consists of hours, minutes and seconds.
    * The range of the value is 00:00:00 (midnight)
    * to 23:59:59 (one second before midnight).
    */
   public class Time
   {
      // The values of the three parts of the time
      private int hours;
      private int minutes;
      private int seconds;

      /**
       * Creates a new Time object set to 00:00:00.
       * Do not change this constructor.
       */
      public Time()
      {
         this.hours = 0;
         this.minutes = 0;
         this.seconds = 0;
      }

      /**
       * Constructor for objects of class Time.
       * Creates a new Time object set to h:m:s.
       * Assumes, without checking, that the parameter values are
       * within bounds.
       * For this task, you don't need to worry about invalid parameter values.
       * Do not change this constructor.
       */
      public Time(int h, int m, int s)
      {
         this.hours = h;
         this.minutes = m;
         this.seconds = s;
      }

      /**
       * Add one second to the current time.
       * When the seconds value reaches 60, it rolls over to zero.
       * When the seconds roll over to zero, the minutes advance.
       * So 00:00:59 rolls over to 00:01:00.
       * When the minutes reach 60, they roll over and the hours advance.
       * So 00:59:59 rolls over to 01:00:00.
       * When the hours reach 24, they roll over to zero.
       * So 23:59:59 rolls over to 00:00:00.
       */
      public void tick()
      {
         // Part a: complete the tick() method
      }

      public String toString()
      {
         return pad(hours) + ":" + pad(minutes) + ":" + pad(seconds);
      }

      /**
       * Returns a string representing the argument value, adding a leading
       * "0" if needed to make it at least two digits long.
       * Do not change this.
       */
      private String pad(int value)
      {
         String sign = "";
         if (value < 0)
         {
            sign = "-";
            value = -1 * value;
          }
          if (value < 10) {
             return sign + "0" + value;
          } else {
             return sign + value;
          }
       }

       public static void main(String[] args)
       {
          Time time = new Time(0,0,0);
          time.tick();
          System.out.println("For (0,0,0) and tick() you got " + time + " which should be 00:00:01");

          time = new Time(0,0, 58);
          time.tick();
          System.out.println("For (0,0,58) and tick() you got " + time + " which should be 00:00:59");

          time = new Time(0,0, 59);
          time.tick();
          System.out.println("For (0,0,59) and tick() you got " + time + " which should be 00:01:00");

          time = new Time(0,58, 59);
          time.tick();
          System.out.println("For (0,58,59) and tick() you got " + time + " which should be 00:59:00");

          time = new Time(0,59, 59);
          time.tick();
          System.out.println("For (0,59,59) and tick() you got " + time + " which should be 01:00:00");

          time = new Time(23,59, 59);
          time.tick();
          System.out.println("For (23,59,59) and tick() you got " + time + " which should be 00:00:00");


       }
    }
    ====
    // Test Code for Lesson 5.14 - FRQ - Time - Part A
    import static org.junit.Assert.*;
    import org.junit.After;
    import org.junit.Before;
    import org.junit.Test;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        private Time[] time = {new Time(0,0,0), new Time(0,0, 58), new Time(0,0, 59), new Time(0,58, 59), new Time(0,59, 59), new Time(23,59, 59)};
        private String[] expected = {"00:00:01", "00:00:59", "00:01:00", "00:59:00", "01:00:00", "00:00:00"};

        @Test
        public void test0() throws IOException
        {
            Time time = new Time(0, 0, 0);
            time.tick();
            String actual = time.toString();
            String expected = "00:00:01";

            boolean passed = getResults(expected, actual, time.toString() +".tick()");
            assertTrue(passed);
        }

        @Test
        public void test1() throws IOException
        {
            int i = 1;
            time[i].tick();
            String actual = time[i].toString();
            boolean passed = getResults(expected[i], actual, time[i].toString() +".tick()");
            assertTrue(passed);
        }

        @Test
        public void test2() throws IOException
        {
            int i = 2;
            time[i].tick();
            String actual = time[i].toString();
            boolean passed = getResults(expected[i], actual, time[i].toString() +".tick()");
            assertTrue(passed);
        }

        @Test
        public void test3() throws IOException
        {
            int i = 3;
            time[i].tick();
            String actual = time[i].toString();
            boolean passed = getResults(expected[i], actual, time[i].toString() +".tick()");
            assertTrue(passed);
        }

        @Test
        public void test4() throws IOException
        {
            int i = 4;
            time[i].tick();
            String actual = time[i].toString();
            boolean passed = getResults(expected[i], actual, time[i].toString() +".tick()");
            assertTrue(passed);
        }

        @Test
        public void test5() throws IOException
        {
            int i = 5;
            time[i].tick();
            String actual = time[i].toString();
            boolean passed = getResults(expected[i], actual, time[i].toString() +".tick()");
            assertTrue(passed);
        }
    }