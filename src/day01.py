'''
------------------------------------------------------------------------------
ADVENT OF CODE 2016 - DAY 1: No Time for a Taxicab
------------------------------------------------------------------------------

Santa's sleigh uses a very high-precision clock to guide its movements, and 
the clock's oscillator is regulated by stars. Unfortunately, the stars have 
been stolen... by the Easter Bunny. To save Christmas, Santa needs you to 
retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each 
day in the Advent calendar; the second puzzle is unlocked when you complete 
the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", 
unfortunately, is as close as you can get - the instructions on the Easter 
Bunny Recruiting Document the Elves intercepted start here, and nobody had 
time to work them out further.

The Document indicates that you should start at the given coordinates (where 
you just landed) and face North. Then, follow the provided sequence: either 
turn left (L) or right (R) 90 degrees, then walk forward the given number of 
blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so 
you take a moment and work out the destination. Given that you can only walk 
on the street grid of the city, how far is the shortest path to the 
destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks 
away.

R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 
2 blocks away.

R5, L5, R5, R3 leaves you 12 blocks away.

How many blocks away is Easter Bunny HQ?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

Then, you notice the instructions continue on the back of the Recruiting 
Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you 
visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?

------------------------------------------------------------------------------
NOTES
------------------------------------------------------------------------------

Read the damn example!

For a good while I was checking whether the place I ENDED UP AT after each
turn had already been visited. However, the puzzle is not asking for this,
as is very clear from the example, if I had only read it properly! This is
the journey in the example, with 'X' being (0, 0):

      4        (4, 4 after 4th instruction, but note that the first place
      4         visited twice is DURING an instruction, at (4, 0), marked
      4         with '#'! I spent WAY too much time not noticing that.)
      4
  X111#1111    (8,0 after 1st instruction)
      4   2
      4   2
      4   2
      33332    (8,-4 after 2nd instruction)
      |   
      (4, -4 after 3rd instruction)

'''

import time

#Timing: Start
start = time.perf_counter()

#Load the puzzle data
with open('txt/day01.txt') as f:
    data = [instruction.strip() for instruction in f.read().split(',')]

#Initialisation
direction = 0 #North (1 = East, and so on)
eastings = 0
northings = 0

#For Part 2 (both parts solved by same code)
visits = [(0, 0)]
part2_solved = False

#Slightly more compact way of calculating movement
walk = {0:(0, 1), 1:(1, 0), 2:(0, -1), 3:(-1, 0)}

#The main loop
for instruction in data:
    dist = int(instruction[1:])
    if instruction[0] == 'L':
        direction = (direction + 3) % 4
    else:
        direction = (direction + 1) % 4

    #We're taking each step one at a time, because we might revisit
    #a location mid-instruction in part 2
    for step in range(dist):
        eastings += walk[direction][0]
        northings += walk[direction][1]
        if (eastings, northings) in visits:
            if not part2_solved:
                part2_solution = f'Part 2: First place visited twice is {abs(eastings) + abs(northings)} blocks away.'
                part2_solved = True
        else:
            visits.append((eastings, northings))

print(f'Part 1: Last place visited is {abs(eastings) + abs(northings)} blocks away.')
print(part2_solution)

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")
