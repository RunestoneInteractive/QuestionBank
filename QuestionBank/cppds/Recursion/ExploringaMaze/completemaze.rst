.. activecode:: completemaze
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Recursion
    :subchapter: ExploringaMaze
    :topics: Recursion/ExploringaMaze
    :from_source: T
    :caption: Complete Maze Solver
    :timelimit: off
    :optional:

    MAZE_OBSTACLE = '+'
    MAZE_START = 'S'
    MAZE_PATH = 'O'
    MAZE_DEAD_END = '-'
    MAZE_TRIED = '.'

    class Maze:
        def __init__(self, mazeFileName):
            # Initialize all of our default variables.
            self.mazeList = []
            self.totalRows = 0
            self.totalColumns = 0

            self.startRow = 0
            self.startColumn = 0

            # And read the maze file.
            self.readMazeFile(mazeFileName)

        def readMazeFile(self, mazeFileName):
            # The maze list is a list of strings.
            # Components of the maze are indicated by specific characters.
            # These characters are listed at the top of the file.

            # The line below says the following:
            # For every line of text in our maze text file, add every single character to a list.
            # The final result is a list of lists, where each element is a single character.
            self.mazeList = [[char for char in line] for line in open(mazeFileName).read().split("\n")]

            # The total number of rows is the total number of strings in the list.
            self.totalRows = len(self.mazeList)

            # The total number of columns is the length of a single line.
            # We can assume all lines of text for the maze are the same length.
            self.totalColumns = len(self.mazeList[0])

            # Lastly, find the start position.
            self.findStartPosition()

        def findStartPosition(self):
            # Iterate through every individual character in the maze list.
            # If we come across the MAZE_START character ('S'),
            # we save the row and column of where it was found, and stop looking.

            # enumerate(...) is very much like using a typical list,
            # except it gives you two pieces of information instead of one.
            # It assumes the format of (index_of_item, item).
            for (row, text) in enumerate(self.mazeList):
                for(column, component) in enumerate(text):
                    if component == MAZE_START:
                        self.startRow = row
                        self.startColumn = column
                        return

        def isOnEdge(self, row, column):
            return (row == 0 or
                    row == self.totalRows - 1 or
                    column == 0 or
                    column == self.totalColumns - 1)

        def print(self):
            for row in self.mazeList:
                # "join" every character in the row into a single string.
                rowText = "".join(row)
                print(rowText)

        # This allows us to use the Maze class like a list, e.g, maze[index]
        def __getitem__(self, index):
            return self.mazeList[index]

    def searchFrom(maze, startRow, startColumn):
        #  Check for base cases:
        #  1. We have run into an obstacle, return false
        if maze[startRow][startColumn] == MAZE_OBSTACLE:
            return False
        #  2. We have found a square that has already been explored
        if maze[startRow][startColumn] == MAZE_TRIED:
            return False

        # 3. Success, an outside edge not occupied by an obstacle
        if maze.isOnEdge(startRow, startColumn):
            maze[startRow][startColumn] = MAZE_PATH
            return True

        maze[startRow][startColumn] = MAZE_TRIED

        # Otherwise, check each cardinal direction (North, south, east, and west).
        # We are checking one space in each direction, thus the plus or minus one below.
        found = searchFrom(maze, startRow - 1, startColumn) or \
                searchFrom(maze, startRow + 1, startColumn) or \
                searchFrom(maze, startRow, startColumn - 1) or \
                searchFrom(maze, startRow, startColumn + 1)

        if found:
            maze[startRow][startColumn] = MAZE_PATH
        else:
            maze[startRow][startColumn] = MAZE_DEAD_END

        return found

    def main():
        maze = Maze("maze1.txt")
        print("Before:")
        maze.print()
        searchFrom(maze, maze.startRow, maze.startColumn)
        print("After:")
        maze.print()

    main()