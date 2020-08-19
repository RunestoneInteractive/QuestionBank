.. activecode:: combo_exercises
    :author: bmiller
    :difficulty: 3.0
    :basecourse: MasteringDatabases
    :chapter: 10QueriesAfterUnary
    :subchapter: 00UnaryCombos
    :topics: 10QueriesAfterUnary/00UnaryCombos
    :from_source: T
    :language: sql
    :include: all_creature_create
    :enabledownload:

    -- 1. Find each non-null achDate of Achievements
    --    whose skillCode = 'PK'.
    /*
    SELECT distinct achDate
    FROM achievement
    WHERE achDate is not NULL and skillCode = 'PK';
    */


    -- 2. How many Creatures achieve skill(s)
    --    in the town whose test_townId = 'mv'?
    SELECT count(creatureId)
    FROM achievement
    WHERE test_townId = 'mv';

    -- 3. Find the skillDescription of of any skill
    --    whose minProficiency is 2.

    -- 4. How many Towns have non-person Creatures
    --    residing in them?

    -- 5. Find each creatureId of Creature who has
    --    achieved in the Town whose test_townId is ‘t’.

    -- 6. How many Roles are there in which
    --    Creatures contributed?

    -- 7. Find the count of Creatures
    --    who have Aspirations.

    -- 8. Find the count the creatures who have
    --    achieved the least skills.

    -- 9. Find the creatureId of each creature
    --    who aspires to achieve 2 or more skills.