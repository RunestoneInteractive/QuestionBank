.. activecode:: oj_test_create
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 14OuterJoin
   :subchapter: NotUsedOJTesting
   :topics: 14OuterJoin/NotUsedOJTesting
   :from_source: T
   :language: sql

   DROP TABLE IF EXISTS Streets;
   CREATE TABLE Streets
    (
      ID INT PRIMARY KEY,
      Name VARCHAR(100)
    );

    DROP TABLE IF EXISTS users;
    CREATE TABLE users
    (
      Username VARCHAR(100) PRIMARY KEY,
      StreetID INT
          REFERENCES Streets ( ID )
    );

    INSERT INTO Streets
    VALUES ( 1, '1st street' ),
      ( 2, '2nd street' ),
      ( 3, '3rd street' ),
      ( 4, '4th street' ),
      ( 5, '5th street' );
    INSERT INTO users
    VALUES ( 'Pol', 1 ),
      ( 'Doortje', 1 ),
      ( 'Marc', 2 ),
      ( 'Bieke', 2 ),
      ( 'Paulien', 2 ),
      ( 'Fernand', 2 ),
      ( 'Pascal', 2 ),
      ( 'Boma', 3 ),
      ( 'Goedele', 3 ),
      ( 'Xavier', 4 );