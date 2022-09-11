'''
------------------------------------------------------------------------------
ADVENT OF CODE 2016 - DAY 18: 
------------------------------------------------------------------------------

As you enter this room, you hear a loud click! Some of the tiles in the floor 
here seem to be pressure plates for traps, and the trap you just triggered 
has run out of... whatever it tried to do to you. You doubt you'll be so lucky 
next time.

Upon closer examination, the traps and safe tiles in this room seem to follow 
a pattern. The tiles are arranged into rows that are all the same width; 
you take note of the safe tiles (.) and traps (^) in the first row (your 
puzzle input).

The type of tile (trapped or safe) in each row is based on the types of the 
tiles in the same position, and to either side of that position, in the 
previous row. (If either side is off either end of the row, it counts as 
"safe" because there isn't a trap embedded in the wall.)

For example, suppose you know the first row (with tiles marked by letters) 
and want to determine the next row (with tiles marked by numbers):

ABCDE
12345

The type of tile 2 is based on the types of tiles A, B, and C; the type 
of tile 5 is based on tiles D, E, and an imaginary "safe" tile. Let's call 
these three tiles from the previous row the left, center, and right tiles, 
respectively. Then, a new tile is a trap only in one of the following 
situations:

Its left and center tiles are traps, but its right tile is not.
Its center and right tiles are traps, but its left tile is not.
Only its left tile is a trap.
Only its right tile is a trap.
In any other situation, the new tile is safe.

Then, starting with the row ..^^., you can determine the next row by 
applying those rules to each new tile:

The leftmost character on the next row considers the left (nonexistent, 
so we assume "safe"), center (the first ., which means "safe"), and 
right (the second ., also "safe") tiles on the previous row. Because 
all of the trap rules require a trap in at least one of the previous 
three tiles, the first tile on this new row is also safe, ..

The second character on the next row considers its left (.), center (.), 
and right (^) tiles from the previous row. This matches the fourth rule: 
only the right tile is a trap. Therefore, the next tile in this new row 
is a trap, ^.

The third character considers .^^, which matches the second trap rule: 
its center and right tiles are traps, but its left tile is not. 
Therefore, this tile is also a trap, ^.

The last two characters in this new row match the first and third 
rules, respectively, and so they are both also traps, ^.

After these steps, we now know the next row of tiles in the room: .^^^^. 
Then, we continue on to the next row, using the same rules, and get ^^..^. 
After determining two new rows, our map looks like this:

..^^.
.^^^^
^^..^

Here's a larger example with ten tiles per row and ten rows:

.^^.^.^^^^
^^^...^..^
^.^^.^.^^.
..^^...^^^
.^^^^.^^.^
^^..^.^^..
^^^^..^^^.
^..^^^^.^^
.^^^..^.^^
^^.^^^..^^

In ten rows, this larger example has 38 safe tiles.

Starting with the map in your puzzle input, in a total of 40 rows (including 
the starting row), how many safe tiles are there?

To begin, get your puzzle input.

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

How many safe tiles are there in a total of 400000 rows?

------------------------------------------------------------------------------
NOTES
------------------------------------------------------------------------------

'''

import time

#Timing: Start
start = time.perf_counter()

#Load data
with open('txt/day18.txt') as f:
    line = f.read().strip()

def apply_rules(s):
    #Rules: Looking at the above rules, if you can avoid worrying about the
    #       leftmost and rightmost tile, the rules down to: tile is a trap
    #       if the previous left and right tiles are different.
    #To avoid catering specifically for the left and right, I've decided to
    # explicitly add 'safe' spaces at the beginning and end of each line

    #Memoization is not worth the cost of looking them up

    rtn = '.'
    for i in range(len(s)-2):
        if s[i] != s[i+2]:
            rtn += '^'
        else:
            rtn += '.'
    return rtn + '.'

def solve(str_solve, n):
    total_safe = str_solve.count('.') - 2
    for i in range(n-1):
        str_solve = apply_rules(str_solve)
        total_safe += str_solve.count('.') - 2
    return total_safe

line = '.' + line + '.'

#Part 1
print(solve(line, 40))

#Part 2
print(solve(line, 400000))

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")