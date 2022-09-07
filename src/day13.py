'''
------------------------------------------------------------------------------
ADVENT OF CODE 2016 - DAY 13: A Maze of Twisty Little Cubicles
------------------------------------------------------------------------------

You arrive at the first floor of this new building to discover a much less 
welcoming environment than the shiny atrium of the last one. Instead, you 
are in a maze of twisty little cubicles, all alike.

Every location in this area is addressed by a pair of non-negative integers 
(x,y). Each such coordinate is either a wall or an open space. You can't move 
diagonally. The cube maze starts at 0,0 and seems to extend infinitely toward 
positive x and y; negative values are invalid, as they represent a location 
outside the building. You are in a small waiting area at 1,1.

While it seems chaotic, a nearby morale-boosting poster explains, the layout 
is actually quite logical. You can determine whether a given x,y coordinate 
will be a wall or an open space using a simple system:

  Find x*x + 3*x + 2*x*y + y + y*y.

Add the office designer's favorite number (your puzzle input).
Find the binary representation of that sum; count the number of bits that 
  are 1.
If the number of bits that are 1 is even, it's an open space.
If the number of bits that are 1 is odd, it's a wall.

For example, if the office designer's favorite number were 10, drawing walls 
as # and open spaces as ., the corner of the building containing 0,0 would 
look like this:

  0123456789
0 .#.####.##
1 ..#..#...#
2 #....##...
3 ###.#.###.
4 .##..#..#.
5 ..##....#.
6 #...##.###

Now, suppose you wanted to reach 7,4. The shortest route you could take is 
marked as O:

  0123456789
0 .#.####.##
1 .O#..#...#
2 #OOO.##...
3 ###O#.###.
4 .##OO#OO#.
5 ..##OOO.#.
6 #...##.###

Thus, reaching 7,4 would take a minimum of 11 steps (starting from your 
current location, 1,1).

What is the fewest number of steps required for you to reach 31,39?

Your puzzle input is 1362.

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

How many locations (distinct x,y coordinates, including your starting 
location) can you reach in at most 50 steps?

------------------------------------------------------------------------------
NOTES
------------------------------------------------------------------------------


'''

import time

#Timing: Start
start = time.perf_counter()

def check_and_add(adj_x, adj_y, adjacents):
    #Make sure we haven't been here before
    if (adj_x, adj_y) not in visited:
        #Is it an open space?
        sum = (adj_x*adj_x) + (3*adj_x) + (2*adj_x*adj_y) + adj_y + (adj_y*adj_y) + 1362
        ones = format(sum, 'b').count('1')
        if (ones % 2) == 0:
            visited.add((adj_x, adj_y))
            adjacents.append((adj_x, adj_y))

def get_adjacents(current_path):
    adjacents = []
    for location in current_path:
        x, y = location
        if x != 0: check_and_add(x-1, y, adjacents)
        if y != 0: check_and_add(x, y-1, adjacents)
        check_and_add(x+1, y, adjacents)
        check_and_add(x, y+1, adjacents)
    return adjacents
    
steps = 0
part2 = 0
visited = set()
here = [(1, 1)]
while (31, 39) not in here:
    steps += 1
    here = get_adjacents(here)
    if steps == 50:
        part2 = len(visited)
print(f'Part 1: {steps}')
print(f'Part 2: {part2}')
print(here)

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
