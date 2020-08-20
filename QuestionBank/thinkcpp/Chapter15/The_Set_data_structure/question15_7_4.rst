.. fillintheblank:: question15_7_4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter15
    :subchapter: The_Set_data_structure
    :topics: Chapter15/The_Set_data_structure
    :from_source: T

    Suppose we have implemented the ``Set`` data structure as defined above, and we run the following code.

    ::

        Set cities(10);
        cities.add("Detroit");
        cities.add("Ann Arbor");
        cities.add("Ann Arbor");
        cities.add("East Lansing");
        cities.add("Grand Rapids");
        cities.add("Detroit");
        cities.add("Mackinac");
        cities.add("Mackinaw");
        string element = cities.getElement(4);  cout << element;

    Type the output exactly as it would appear in the terminal.

    - :(Mackinac):
      :.*: Incorrect! Try modifying the active code!