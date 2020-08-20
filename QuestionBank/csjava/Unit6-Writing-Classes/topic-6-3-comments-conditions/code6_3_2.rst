.. activecode:: code6_3_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit6-Writing-Classes
    :subchapter: topic-6-3-comments-conditions
    :topics: Unit6-Writing-Classes/topic-6-3-comments-conditions
    :from_source: T
    :language: java
    :autograde: unittest

    // comments?
    public class User
    {

      private String username;
      private String password;

      public User()
      {
         username = "guest";
         password = "guest" + (int)(Math.random()*1000);
      }

      public User(String nameInit, String pwordInit)
      {
          username = nameInit;
          password = pwordInit;
      }

      public void welcome()
      {
         System.out.println("Welcome " + username + "!");
      }

      public static void main(String[] args)
      {
          User u1 = new User(); // guest login
          // new user
          User u2 = new User("cooldude@gmail.com", "Coolness*10");
          u1.welcome();
          u2.welcome();
      }
    }
    ====
    // Test for 5.3.5 Comments
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    import java.nio.file.Files;
    import java.nio.file.Paths;

    public class RunestoneTests extends CodeTestHelper
    {
        private String program;

        @Test
        public void testMain()
        {
            String output = getMethodOutput("main");
            String expect = "Welcome guest!\nWelcome cooldude@gmail.com!";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }

        @Test
        public void testClassComment() {
            program = getCodeWithComments();

            int index = program.indexOf("public class User");

            String beginning = program.substring(0, index-1).trim();
            String expected = "A comment starting with // or /* and not // comments?";
            //System.out.println(beginning);

            boolean pass = !beginning.startsWith("// comments") && isComment(beginning);

            boolean passed = getResults(expected, beginning, "Class comment", pass);
            assertTrue(passed);
        }

        @Test
        public void testVariablesComment() {
            program = getCodeWithComments();

            int start = program.indexOf("{") + 1;
            int end = program.indexOf("private String username");

            String comment = program.substring(start, end).trim();
            String expected = "A comment starting with // or /*";
            //System.out.println(beginning);

            boolean passed = getResults(expected, comment, "Variable comment", isComment(comment));
            assertTrue(passed);
        }

        @Test
        public void testDefaultConstructorComment() {
            program = getCodeWithComments();

            int start = program.indexOf("password;") + "password;".length() + 1;
            int end = program.indexOf("public User()");

            String comment = program.substring(start, end).trim();
            String expected = "A comment starting with // or /*";
            //System.out.println(beginning);

            boolean passed = getResults(expected, comment, "Default constructor comment", isComment(comment));
            assertTrue(passed);
        }

        @Test
        public void testConstructorComment() {
            program = getCodeWithComments();

            int start = program.indexOf("*1000);");
            start = program.indexOf("}", start) + 1;
            int end = program.indexOf("public User(String nameInit, String pwordInit)");

            String comment = program.substring(start, end).trim();
            String expected = "A comment starting with // or /*";
            //System.out.println(beginning);

            boolean passed = getResults(expected, comment, "Constructor comment", isComment(comment));
            assertTrue(passed);
        }

        @Test
        public void testWelcomeComment() {
            program = getCodeWithComments();

            int start = program.indexOf("password = pwordInit;");
            start = program.indexOf("}", start) + 1;
            int end = program.indexOf("public void welcome()");

            String comment = program.substring(start, end).trim();
            String expected = "A comment starting with // or /*";
            //System.out.println(beginning);

            boolean passed = getResults(expected, comment, "Welcome method comment", isComment(comment));
            assertTrue(passed);
        }

        @Test
        public void testMainComment() {
            program = getCodeWithComments();

            int start = program.indexOf("username + \"!\");");
            start = program.indexOf("}", start) + 1;
            int end = program.indexOf("public static void main");

            String comment = program.substring(start, end).trim();
            String expected = "A comment starting with // or /*";
            //System.out.println(beginning);

            boolean passed = getResults(expected, comment, "Main method comment", isComment(comment));
            assertTrue(passed);
        }

        private boolean isComment(String block) {
            if (!block.contains("\n") && block.startsWith("//"))
                return true;
            if (block.startsWith("/*") && block.endsWith("*/"))
                return true;
            return false;

        }
    }