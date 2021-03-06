.. activecode:: ccs_maze08
   :author: Michael McCarrin
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Selection
   :subchapter: Exercises
   :topics: Selection/Exercises
   :from_source: F
   :include: ccs_maze00, ccs_maze01, ccs_maze02, ccs_maze03, ccs_maze04, ccs_maze05, ccs_maze06, ccs_maze07
   :datafile: :maze1a.txt

   This is the main part of the program. It calls the other functions, which work
   together to solve the maze. You should not need to edit it except to
   add temporary test code,\* but you **should** run this code each time you
   implement a new function to make sure everything is working correctly.
   
   \*The one exception is that if you decide to try the methodical_walker
   function you will need to comment out the random_walker line and
   uncomment the methodical walker line instead. 
   ~~~~
   '''
   This main section is provided for your convenience.
   This code allows you to input a maze from a designated text file.
   '''
   solved = False
       
   filename = input("Enter Maze Filename:")
           
   # STEP 0: read the maze as a string using get_maze()
   maze_s = get_maze(filename)
   print(maze_s) # PRINT STATEMENT TO TEST GET_MAZE. DELETE AFTER TESTING.
    
   # STEP 1: convert the maze to a list using convert()
   maze = convert(maze_s)
    
   if maze:
       print("Maze to be solved:" )
       # STEP 2: display the converted maze to the screen using display()
       display(maze)
    
   # STEP 3: find the coordinates of the Start using find_cell()  
   start = find_cell(maze, START)
    
   # STEP 4: find the coordinates of the Goal using find_cell()  
   goal = find_cell(maze, GOAL)
    
   # STEP 5: Solve the maze with one of the walker functions. (Start with
   #         random_walker() first).
   if (start and goal):
       solution_path = random_walker(maze, start, goal)
   
       # STEP 7: When you are ready to try methodical_walker uncomment the line below. 
       #solution_path = methodical_walker(maze, start, goal)
       if (solution_path and solution_path[-1] == goal): # If we made it to the end...
           solved = True
           
   if solved == True:
       print("Solution:")
       # STEP 6: Display the solution using display_with_path()
       display_with_path(maze,solution_path)
   else:
       print("Sorry. We did not escape the maze.")
   ====