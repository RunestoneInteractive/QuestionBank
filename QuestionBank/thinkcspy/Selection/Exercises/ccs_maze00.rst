.. activecode:: ccs_maze00
    :author: Michael McCarrin
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Selection
    :subchapter: Exercises
    :topics: Selection/Exercises
    :from_source: F
    :include: ccs_mazes

    from random import choice
    
    MAX_TRIES = 100000
    
    OPEN_S    = '-'
    BLOCKED_S = '#'
    START_S   = 'S'
    GOAL_S    = 'G'
    PATH_S    = '*'
    
    OPEN    = 0 
    BLOCKED = 1
    START   = 2
    GOAL    = 3
    PATH    = 4
    
    ### +++++++++++++++++++++++++++++++++++++++ ###
    ###   Helper function to get maze string    ###
    ###   from a file                           ###
    def get_maze(filename):
        maze_s = mazes[filename]
        return maze_s
    ###                                         ###
    ### +++++++++++++++++++++++++++++++++++++++ ###
    '''
    Convert the given string representation of a maze to
    the list representation, a list of lists of integers
    
    Parameter: String representation of maze
               E.g. "--S---\n##-##-\n-#-#--\n---#G#\n###---"
           
    Return:    A list of lists of integers
               E.g. [[0,0,2,0,0,0],[1,1,0,1,1,0],[0,1,0,1,0,0],[0,0,0,1,3,1],[1,1,1,0,0,0]]
    '''
    def convert(maze_s):
        # ADD CODE HERE
     
        maze = []  # MODIFY THIS
    
        return maze

    '''
    Return the position of a given cell (START or GOAL) in the maze
    
    Parameter: maze - the maze (list represenation) 
               cell - either START or GOAL
           
    Return:    the position of the specified cell as a two-item list, [row,col]; 
               returns an empty list [] if cell is not START or GOAL
    '''
    def find_cell(maze, cell_type):
        position = [] 
        # ADD CODE HERE
        return position

    '''
    Given the position of a cell, return a list of the neighbors that are not
    blocked by walls.
    
    Parameter: maze - the maze (list represenation)
               position - a two-item list containing the row and column of any
               open cell in the maze. At most it will have four options (if
               all directions are open), and at the least the list will
               contain 1 option.
           
    Return:    A list of two-item cells that are either above, below, to the
               left or to the right of the given cell and are not occupied
               by walls.
    '''

    def look_around(maze, position):
        # find the boundaries of the maze
        maxrow = len(maze)-1
        maxcol = len(maze[0])-1
    
        # put row and col into variables for readability
        row,col    = position
    
        # set up empty lists for later 
        candidates = []
        options    = []

        # first add anything that's inside the maze grid 
        if row+1 <=maxrow:
            candidates += [[row + 1,col]]
        if row-1 >= 0:
            candidates += [[row - 1,col]]
        if col+1 <=maxcol:
            candidates += [[row,col+1]]
        if col-1 >= 0:
            candidates += [[row,col-1]]

        # Now weed out blocked cells
        for cell in candidates:
            row,col = cell
            if maze[row][col] != BLOCKED:
                options += [cell]
    
        return options 

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


    '''
    Find the solution path from START cell to GOAL cell. This function
    differs from random_walker in that it remembers where it has
    been and does not go back to parts of the maze it has already
    explored unless it hits a dead end. If it has to backtrack, it
    removes the bad decision from its path. As a consequence, all
    the cells in the final path advance toward the goal.
    
    Parameter: maze  - the maze (list representation) to search
               start - position of the start cell
               goal  - position of the goal cell
           
    Return:    the path  (list of [r,c]) from START to GOAL
               for this algorithm, the returned path is the solution path, 
               a shortest path from start to goal
    '''
    def methodical_walker(maze, start, goal):
        path = [] 
        # ADD CODE HERE
    
        return path
    
    '''
    Given a list representation of the maze, this function 
    creates the corresponding string representation and prints it
    to the screen.
    
    Parameter: maze  - the maze (list representation) to display
           
    Return:    None
    '''
    def display(maze):
        # ADD CODE HERE
        print("display() not yet implemented") # MODIFY THIS
    
    '''
    Given a list representation of the maze and a path, this 
    function creates the corresponding string representation 
    and prints it to the screen. Cells that are part of the
    path should be marked with a `*'
    
    Parameter: maze  - the maze (list representation) to display
               path  - the path (list of [row,col]) to display
           
    Return:    None
    '''
    def display_with_path(maze, path):
        # ADD CODE HERE 
        print("display_with_path() not yet implemented") # MODIFY THIS
    
    ### ******************* M A I N ******************* ###
    
    '''
    This main control loop is provided for your convenience.
    This code allows you to input a maze from a designated text file.
    '''
    
    if __name__ == "__main__":
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