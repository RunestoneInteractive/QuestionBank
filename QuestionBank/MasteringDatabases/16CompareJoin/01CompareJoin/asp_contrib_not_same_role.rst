.. activecode:: asp_contrib_not_same_role
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 16CompareJoin
   :subchapter: 01CompareJoin
   :topics: 16CompareJoin/01CompareJoin
   :from_source: T
   :language: sql
   :include: all_creature_create

   -- Find each creature who aspires to contribute and
   -- contributed the same skillCode to a team where
   -- their contributed roleName is not the same as their aspired roleName.
   --
   SELECT C.*, A.skillCode aspContrib_skillCode, A.roleName aspContrib_roleName
   FROM contribution C, aspiredContribution A
   WHERE C.creatureId = A.creatureId
   AND   C.skillCode = A.skillCode
   AND C.roleName != A.roleName   -- this is the 'compare'
   ;