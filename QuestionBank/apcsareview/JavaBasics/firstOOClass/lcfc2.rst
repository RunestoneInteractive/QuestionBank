.. activecode:: lcfc2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: JavaBasics
   :subchapter: firstOOClass
   :topics: JavaBasics/firstOOClass
   :from_source: T
   :language: java
   :tour_1: "Introductory Tour"; 1-2: person_line1-2; 4-5: person_line4-5; 8-12: person_line8-12; 15-18: person_line15-18; 19-22: person_line19-22; 24-27: person_line24-27; 29-32: person_line29-32; 34-35: person_line34-35; 39-45: person_line39-45; 47: person_line47;

   public class Person
   {
     /// fields ////////////////
     private String name;
     private String cell;

     /////// constructors ////////////////////
     public Person(String theName, String theCell)
     {
       this.name = theName;
       this.cell = theCell;
     }

     //////////// methods ///////////////////////
     public String getName()
     {
        return this.name;
     }
     public void setName(String theName)
     {
        this.name = theName;
     }

     public String getCell()
     {
        return this.cell;
     }

     public void setCell(String theCell)
     {
        this.cell = theCell;
     }

     public String toString() { return "name: " + this.name +
                                ", cell: " + this.cell; }


     //////////// main for testing //////////////
     public static void main(String[] args)
     {
       Person p1 = new Person("Deja", "555 132-3253");
       System.out.println(p1);
       Person p2 = new Person("Avery", "555 132-6632");
       System.out.println(p2);
     }

   }