'''
------------------------------------------------------------------------------
ADVENT OF CODE 2016 - DAY 3: Squares With Three Sides
------------------------------------------------------------------------------

Now that you can think clearly, you move deeper into the labyrinth of 
hallways and office furniture that makes up this part of Easter Bunny HQ. 
This must be a graphic design department; the walls are covered in 
specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, 
but... 5 10 25? Some of these aren't triangles. You can't help but mark the 
impossible ones.

In a valid triangle, the sum of any two sides must be larger than the 
remaining side. For example, the "triangle" given above is impossible, 
because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

Now that you've helpfully marked up their design documents, it occurs to you 
that triangles are specified in groups of three vertically. Each set of three 
numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds 
digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603

In your puzzle input, and instead reading by columns, how many of the listed 
triangles are possible?

------------------------------------------------------------------------------
NOTES
------------------------------------------------------------------------------


'''

import time

#Timing: Start
start = time.perf_counter()

def check_tri(tri):
    x, y, z = sorted(tri)
    if (x + y) > z:
        return 1
    return 0

part1_possibles = 0
part2_possibles = 0
with open('txt/day03.txt') as f:
    lines = []
    for line in f:

        #Part 1 is fairly straightforward
        part1_possibles += check_tri(int(i) for i in line.split())

        #For Part 2, we look at three lines at a time:
        lines.append([int(i) for i in line.split()])
        if len(lines) == 3:
            t1 = [lines[0][0], lines[1][0], lines[2][0]]
            t2 = [lines[0][1], lines[1][1], lines[2][1]]
            t3 = [lines[0][2], lines[1][2], lines[2][2]]
            part2_possibles += check_tri(t1) + check_tri(t2) + check_tri(t3)
            lines = []

print(part1_possibles)
print(part2_possibles)

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
