.. activecode:: challenge-9-1-online-store
  :author: bmiller
  :difficulty: 3
  :basecourse: csjava
  :topics: Unit9-Inheritance/topic-9-1-inheritance-day2
  :from_source: T
  :language: java

  Declare 3 instance variables for each of the classes below. Create an inheritance or association relationship for some of them.
  ~~~~
  class ItemForSale
  {

  }

  class Movie
  {

  }

  class Book
  {

  }

  class Author
  {

  }

  public class Store
  {
       // instance variables

       public static void main(String[] args)
       {
          Store s = new Store();
          Book b = new Book();
          System.out.println(b instanceof ItemForSale);
       }
  }