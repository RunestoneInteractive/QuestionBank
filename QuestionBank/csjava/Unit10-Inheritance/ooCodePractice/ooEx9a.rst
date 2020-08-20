.. activecode::  ooEx9a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit10-Inheritance
   :subchapter: ooCodePractice
   :topics: Unit10-Inheritance/ooCodePractice
   :from_source: T
   :language: java

   public class Store
   {
       private String name;
       private String address;

       public Store(String theName, String theAddress)
       {
           this.name = theName;
           this.address = theAddress;
       }

       public String getName() { return this.name; }
       public String getAddress() { return this.address; }
       public void setName(String theName) { this.name = theName; }
       public void setAddress(String theAddress) { this.address = theAddress; }

       public String toString() { return this.name + "\n" + this.address; }

       public static void main(String[] args)
       {
           Store myStore = new Store("Barb's Store", "333 Main St.");
           System.out.println(myStore);
           myStore.setName("Barbara's Store");
           myStore.setAddress("555 Pine St.");
           System.out.println(myStore);

       }
   }