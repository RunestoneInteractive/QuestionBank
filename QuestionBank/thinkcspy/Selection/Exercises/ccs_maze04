.. activecode:: ccs_maze04
   :author: Michael McCarrin
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Selection
   :subchapter: Exercises
   :topics: Selection/Exercises
   :from_source: F
   :include: ccs_maze00, ccs_maze03
   
   random_walker function. Read the "TODO" comments and implement according to the specification.
   ~~~~
   '''
   Find a path from START cell to GOAL cell by wandering randomly
   until you find the exit

   Parameter: maze  - the maze (list representation) to search
              start - position of the start cell
              goal  - position of the goal cell
              
   Return:    the path  (list of [r,c]) from START to GOAL
              for this algorithm, the returned path is a list of all visited cells
   '''
   def random_walker(maze, start, goal):
       path = [] # Start with an empty path
       current_position = start
       for attempt in range(MAX_TRIES): 
           # \TODO STEP 1: add current position to the path
           # \TODO STEP 2: get options (hint: use look_around)
           # \TODO STEP 3: pick an option at random using choice()
           # \TODO STEP 4: update the current position to the option you picked

           if current_position == goal: # if this is true you solved the maze
               path += [goal]           # so add the last cell
               break                    # and quit searching

   
       return path
   ====