'''
------------------------------------------------------------------------------
ADVENT OF CODE 2016 - DAY 19: An Elephant Named Joseph
------------------------------------------------------------------------------

The Elves contact you over a highly secure emergency channel. Back at the 
North Pole, the Elves are busy misunderstanding White Elephant parties.

Each Elf brings a present. They all sit in a circle, numbered starting with 
position 1. Then, starting with the first Elf, they take turns stealing all 
the presents from the Elf to their left. An Elf with no presents is removed 
from the circle and does not take turns.

For example, with five Elves (numbered 1 to 5):

  1
5   2
 4 3

Elf 1 takes Elf 2's present.
Elf 2 has no presents and is skipped.
Elf 3 takes Elf 4's present.
Elf 4 has no presents and is also skipped.
Elf 5 takes Elf 1's two presents.
Neither Elf 1 nor Elf 2 have any presents, so both are skipped.
Elf 3 takes Elf 5's three presents.

So, with five Elves, the Elf that sits starting in position 3 gets all the 
presents.

With the number of Elves given in your puzzle input, which Elf gets all the 
presents?

------------------------------------------------------------------------------
PART 2
------------------------------------------------------------------------------

Realizing the folly of their present-exchange rules, the Elves agree to 
instead steal presents from the Elf directly across the circle. If two Elves 
are across the circle, the one on the left (from the perspective of the 
stealer) is stolen from. The other rules remain unchanged: Elves with no 
presents are removed from the circle entirely, and the other elves move in 
slightly to keep the circle evenly spaced.

For example, with five Elves (again numbered 1 to 5):

The Elves sit in a circle; Elf 1 goes first:

  1
5   2
 4 3

Elves 3 and 4 are across the circle; Elf 3's present is stolen, being the one 
to the left. Elf 3 leaves the circle, and the rest of the Elves move in:

  1           1
5   2  -->  5   2
 4 -          4

Elf 2 steals from the Elf directly across the circle, Elf 5:

  1         1 
-   2  -->     2
  4         4 

Next is Elf 4 who, choosing between Elves 1 and 2, steals from Elf 1:

 -          2  
    2  -->
 4          4

Finally, Elf 2 steals from Elf 4:

 2
    -->  2  
 -

So, with five Elves, the Elf that sits starting in position 2 gets all the 
presents.

With the number of Elves given in your puzzle input, which Elf now gets 
all the presents?

------------------------------------------------------------------------------
NOTES
------------------------------------------------------------------------------

Your puzzle input is 3014603.

'''

import time
from collections import deque

#Timing: Start
start = time.perf_counter()

def solve_part1(n):
    i = 1
    while True:
        if (2 ** i) > n:
            break
        i += 1
    start = 2 ** (i-1)
    diff = n - start
    return (diff*2) + 1

def solve_part2(n):
    i = 1
    l = deque()
    r = deque()
    half = ((n + 1) // 2) 
    while i <= half:
        l.append(i)
        r.appendleft(i+half)
        i += 1
    if (n % 2): r.popleft()
    
    while l and r:
        if len(l) > len(r):
            l.pop()
        else:
            r.pop()
        #Rotate
        r.appendleft(l.popleft())
        l.append(r.pop())
    if len(l):
        return l[0]
    else:
        return r[0]

print(solve_part1(3014603))
print(solve_part2(3014603))

#Timing: End
end = time.perf_counter()
print(f"Time to complete = {str((end-start)*1000)} milliseconds.")